
"""
Pipeline M2 para detecção candidata de rachaduras em paredes.

Execução na raiz do projeto:
    python src/main.py

O resultado é uma segmentação candidata para inspeção visual.
Não representa diagnóstico estrutural.
"""

from pathlib import Path
import argparse
import csv

import cv2
import numpy as np


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT = ROOT / "images" / "input"
DEFAULT_OUTPUT = ROOT / "images" / "results_m2"


def segment_cracks(
    image,
    threshold=18,
    min_area=12,
    kernel_size=9,
    close_iterations=1
):
    """
    Segmenta estruturas escuras usando black-hat morfológico.

    Retorna:
    - imagem em escala de cinza;
    - resposta black-hat;
    - máscara binária inicial;
    - máscara final filtrada;
    - lista de componentes conectados.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    kernel_size = max(3, int(kernel_size) | 1)

    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (kernel_size, kernel_size)
    )

    blackhat = cv2.morphologyEx(
        gray,
        cv2.MORPH_BLACKHAT,
        kernel
    )

    _, binary = cv2.threshold(
        blackhat,
        int(threshold),
        255,
        cv2.THRESH_BINARY
    )

    close_kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (3, 3)
    )

    closed = cv2.morphologyEx(
        binary,
        cv2.MORPH_CLOSE,
        close_kernel,
        iterations=max(0, int(close_iterations))
    )

    number_labels, labels, stats, centroids = (
        cv2.connectedComponentsWithStats(
            closed,
            connectivity=8
        )
    )

    filtered = np.zeros_like(closed)

    components = []

    for label in range(1, number_labels):

        x, y, width, height, area = stats[label]

        if area >= int(min_area):

            filtered[labels == label] = 255

            aspect_ratio = (
                max(width, height) /
                max(1, min(width, height))
            )

            components.append({
                "label": int(label),
                "x": int(x),
                "y": int(y),
                "width": int(width),
                "height": int(height),
                "area_px": int(area),
                "aspect_ratio": round(
                    float(aspect_ratio),
                    3
                )
            })

    return (
        gray,
        blackhat,
        binary,
        filtered,
        components
    )


def save_components(components, output_path):

    fieldnames = [
        "label",
        "x",
        "y",
        "width",
        "height",
        "area_px",
        "aspect_ratio"
    ]

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(components)


def run(input_dir, output_dir):

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    rows = []

    image_files = sorted(
        path
        for path in input_dir.iterdir()
        if path.suffix.lower() in {
            ".png",
            ".jpg",
            ".jpeg"
        }
    )

    if not image_files:

        raise SystemExit(
            f"Nenhuma imagem encontrada em {input_dir}"
        )

    for path in image_files:

        image = cv2.imread(str(path))

        if image is None:

            print(
                f"Imagem ignorada: {path.name}"
            )

            continue

        # Baseline da M1: Canny

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        blur = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

        canny = cv2.Canny(
            blur,
            50,
            150
        )

        cv2.imwrite(
            str(output_dir / f"{path.stem}_canny.png"),
            canny
        )

        # Comparação controlada:
        # somente o limiar black-hat muda.

        configurations = {
            "A": 12,
            "B": 24
        }

        for config, threshold in configurations.items():

            (
                gray,
                blackhat,
                binary,
                mask,
                components
            ) = segment_cracks(
                image,
                threshold=threshold,
                min_area=12,
                kernel_size=9,
                close_iterations=1
            )

            # Salvar resultados intermediários

            cv2.imwrite(
                str(
                    output_dir /
                    f"{path.stem}_blackhat_{config}.png"
                ),
                blackhat
            )

            cv2.imwrite(
                str(
                    output_dir /
                    f"{path.stem}_binary_{config}.png"
                ),
                binary
            )

            cv2.imwrite(
                str(
                    output_dir /
                    f"{path.stem}_mask_{config}.png"
                ),
                mask
            )

            # Sobreposição das regiões candidatas em vermelho

            overlay = image.copy()

            overlay[mask > 0] = (0, 0, 255)

            overlay = cv2.addWeighted(
                image,
                0.68,
                overlay,
                0.32,
                0
            )

            cv2.imwrite(
                str(
                    output_dir /
                    f"{path.stem}_overlay_{config}.png"
                ),
                overlay
            )

            # Métricas descritivas

            foreground_pixels = int(
                np.count_nonzero(mask)
            )

            foreground_fraction = (
                foreground_pixels / mask.size
            )

            largest_component = max(
                [
                    component["area_px"]
                    for component in components
                ],
                default=0
            )

            rows.append({
                "image_id": path.name,
                "configuration": config,
                "blackhat_threshold": threshold,
                "min_component_area_px": 12,
                "kernel_size_px": 9,
                "close_iterations": 1,
                "foreground_pixels": foreground_pixels,
                "foreground_fraction": round(
                    foreground_fraction,
                    6
                ),
                "component_count": len(components),
                "largest_component_area_px": largest_component
            })

            # Salvar tabela de componentes

            save_components(
                components,
                output_dir /
                f"{path.stem}_components_{config}.csv"
            )

    # Resumo experimental

    if rows:

        with open(
            output_dir / "experiment_summary.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=list(rows[0].keys())
            )

            writer.writeheader()
            writer.writerows(rows)

    print(
        f"Processamento concluído: "
        f"{len(image_files)} imagem(ns)."
    )

    print(
        f"Resultados salvos em: {output_dir}"
    )

    print(
        "A proporção de pixels e os componentes "
        "são indicadores descritivos. "
        "Não representam acurácia sem máscaras "
        "de referência anotadas."
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT
    )

    args = parser.parse_args()

    run(
        args.input,
        args.output
    )

import cv2
import os