
# Dataset — Detecção de Rachaduras em Paredes

## 1. Descrição

O conjunto de imagens utilizado neste projeto é composto por cinco fotografias de paredes com estruturas visuais que podem representar rachaduras.

As imagens foram mantidas do projeto M1 para garantir continuidade entre as etapas.

## 2. Organização

As imagens estão armazenadas em:

`images/input/`

| ID | Arquivo | Uso |
|---|---|---|
| Img1 | Img1.png | Desenvolvimento e avaliação preliminar |
| Img2 | Img2.png | Desenvolvimento e avaliação preliminar |
| Img3 | Img3.png | Desenvolvimento e avaliação preliminar |
| Img4 | Img4.png | Desenvolvimento e avaliação preliminar |
| Img5 | Img5.png | Desenvolvimento e avaliação preliminar |

Quantidade total: 5 imagens.

## 3. Origem e condições de aquisição

A origem individual, autoria, licença e condições de aquisição das imagens devem ser confirmadas com base nos registros da equipe produzidos durante a M1.

Essas informações não podem ser determinadas apenas pela análise dos arquivos PNG.

Antes da redistribuição pública, a equipe deverá verificar se possui autorização para compartilhar as imagens.

## 4. Critérios de seleção

As imagens foram selecionadas por apresentarem estruturas visuais compatíveis com o problema de detecção de rachaduras em paredes.

O conjunto permite observar situações distintas de:

- contraste entre rachadura e parede;
- iluminação;
- textura superficial;
- espessura das estruturas;
- presença de ruído visual.

O conjunto é pequeno e não representa todas as condições encontradas em paredes reais.

## 5. Protocolo experimental

As cinco imagens são processadas pelas duas configurações do experimento M2.

Configuração A:
- Limiar black-hat: 12;
- Kernel elíptico: 9 × 9;
- Área mínima: 12 pixels;
- Fechamento morfológico: kernel 3 × 3;
- Uma iteração.

Configuração B:
- Limiar black-hat: 24;
- Kernel elíptico: 9 × 9;
- Área mínima: 12 pixels;
- Fechamento morfológico: kernel 3 × 3;
- Uma iteração.

A única variável alterada entre as configurações é o limiar black-hat.

## 6. Referência manual

Na versão M2, não há máscaras de referência manual validadas.

Por esse motivo, os resultados quantitativos atuais descrevem a saída do algoritmo, mas não permitem calcular diretamente a precisão da segmentação.

Para a M3, serão produzidas máscaras binárias de referência, com pixels de rachadura marcados em branco e demais regiões em preto.

As máscaras deverão ser revisadas por integrantes da equipe.

## 7. Limitações

- Apenas cinco imagens;
- Proveniência e licença precisam ser confirmadas;
- Ausência de máscaras de referência validadas;
- Possibilidade de confusão entre rachaduras, sombras e textura;
- Parâmetros preliminares;
- Ausência de escala física para medir rachaduras em milímetros.