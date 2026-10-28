
# Detecção de Rachaduras em Paredes — M2

Projeto Aplicado Longitudinal da disciplina de Processamento de Imagens.

Grupo 15 — UNIVALI.

## Integrantes

- Gustavo Koerich Cardoso
- Iago Fermiano Orsi
- Igor Orsi Dalagnello

## Problema

O projeto investiga técnicas de processamento digital de imagens para localizar e destacar possíveis rachaduras em paredes.

Na M1, foi desenvolvido um sistema inicial utilizando o algoritmo Canny.

Na M2, o sistema evoluiu para um pipeline de realce morfológico, segmentação, filtragem e análise de componentes conectados.

O resultado é uma máscara candidata para inspeção visual, não um diagnóstico de segurança estrutural.

## Objetivos

- Realçar possíveis rachaduras;
- Segmentar regiões candidatas;
- Aplicar operações morfológicas;
- Analisar componentes conectados;
- Extrair características geométricas;
- Comparar configurações experimentais;
- Produzir resultados verificáveis.

## Estado atual

### Implementado na M2

- Leitura de imagens;
- Conversão para escala de cinza;
- Suavização Gaussiana;
- Canny como baseline da M1;
- Black-hat morfológico;
- Limiarização;
- Fechamento morfológico;
- Análise de componentes conectados;
- Filtragem por área;
- Extração de características;
- Geração de máscaras;
- Geração de sobreposições;
- Exportação de resultados CSV;
- Comparação entre limiares 12 e 24.

### Planejado para a M3

- Produção de máscaras de referência;
- Cálculo de IoU e Dice;
- Cálculo de precisão e revocação;
- Avaliação em imagens reservadas;
- Calibração de parâmetros;
- Revisão final da documentação.

## Pipeline

Imagem original
→ escala de cinza
→ filtro Gaussiano
→ black-hat morfológico
→ limiarização
→ fechamento morfológico
→ componentes conectados
→ filtragem por área
→ máscara final
→ extração de características.

O Canny é executado separadamente como baseline.

## Dados

As cinco imagens utilizadas estão em:

`images/input/`

O inventário e o protocolo experimental estão em:

`docs/dataset.md`

A origem e a licença das imagens devem ser confirmadas pela equipe antes da redistribuição.

## Instalação

Requisitos:

- Python 3.10 ou superior;
- OpenCV;
- NumPy.

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Na raiz do projeto:

```bash
python src/main.py
```

Também é possível definir os diretórios:

```bash
python src/main.py --input images/input --output images/results_m2
```

## Resultados

Os resultados são salvos em:

`images/results_m2/`

Arquivos gerados:

- `*_canny.png`: baseline;
- `*_blackhat_A.png`: realce morfológico A;
- `*_blackhat_B.png`: realce morfológico B;
- `*_binary_A.png`: segmentação inicial A;
- `*_binary_B.png`: segmentação inicial B;
- `*_mask_A.png`: máscara final A;
- `*_mask_B.png`: máscara final B;
- `*_overlay_A.png`: sobreposição A;
- `*_overlay_B.png`: sobreposição B;
- `*_components_A.csv`: características A;
- `*_components_B.csv`: características B;
- `experiment_summary.csv`: resumo experimental.

Os indicadores atuais são descritivos. Sem máscaras de referência, não representam acurácia ou precisão da segmentação.

## Documentação

- [Proposta M1](docs/proposta.md)
- [Revisão M1 e plano M2](docs/revisao_m1_plano_m2.md)
- [Dataset e protocolo](docs/dataset.md)
- [Relatório M2](docs/relatorio_m2.md)

## Estrutura

```text
.
├── README.md
├── requirements.txt
├── src/
│   └── main.py
├── docs/
│   ├── proposta.md
│   ├── revisao_m1_plano_m2.md
│   ├── dataset.md
│   └── relatorio_m2.md
├── images/
│   ├── input/
│   ├── results/
│   └── results_m2/
└── notebooks/
```

## Contribuições

As contribuições dos integrantes devem ser registradas considerando implementação, experimentos, dados, documentação, revisão e análise.

A divisão de tarefas deve refletir as atividades efetivamente realizadas.

## Uso de IA

ChatGPT foi utilizado como apoio à organização da documentação, elaboração e revisão de código e estruturação dos experimentos.

Os integrantes são responsáveis pela execução, validação e compreensão dos materiais entregues.

## Referências

- OpenCV Documentation: https://docs.opencv.org/
- Gonzalez e Woods — Digital Image Processing.
- Bradski e Kaehler — Learning OpenCV.

## Vídeo M2

https://youtu.be/BmqG4DorHOQ

# Vídeo da M1

Link do vídeo (YouTube Não Listado):

```text
https://youtu.be/5gtmJQ07VWs
```
