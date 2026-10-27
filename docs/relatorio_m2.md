
# Relatório M2 — Detecção de Rachaduras em Paredes

**Disciplina:** Processamento de Imagens  
**Projeto Aplicado Longitudinal — Etapa M2**  
**Grupo:** Igor Orsi Dallagnelo, Gustavo Koerich Cardoso e Iago Fermiano Orsi

## 1. Introdução

O projeto tem como objetivo investigar técnicas de processamento digital de imagens para detectar e destacar rachaduras visíveis em paredes.

Na M1, foi desenvolvido um sistema inicial utilizando o algoritmo Canny para detecção de bordas.

Embora o Canny permita localizar descontinuidades de intensidade, ele também identifica bordas de texturas, manchas e outros elementos que não correspondem necessariamente a rachaduras.

Na M2, o projeto evoluiu para uma abordagem baseada em realce morfológico, segmentação binária e análise de componentes conectados.

O sistema produz regiões candidatas para inspeção visual. Ele não realiza diagnóstico de segurança estrutural.

## 2. Objetivos

### 2.1 Objetivo geral

Desenvolver uma implementação parcial executável capaz de destacar possíveis rachaduras em imagens de paredes e produzir resultados verificáveis.

### 2.2 Objetivos específicos

- Manter o Canny como método de referência da M1;
- Implementar realce de estruturas escuras utilizando black-hat;
- Realizar segmentação por limiarização;
- Aplicar fechamento morfológico;
- Analisar componentes conectados;
- Extrair características geométricas;
- Comparar duas configurações de limiar;
- Registrar resultados em imagens e arquivos CSV;
- Identificar limitações e planejar a conclusão na M3.

## 3. Evolução desde a M1

A M1 apresentou uma implementação inicial baseada em Canny.

O feedback recebido indicou a necessidade de evoluir o processamento para além da detecção genérica de bordas.

Na M2, foram incorporadas:

- Segmentação de estruturas escuras;
- Operações morfológicas;
- Filtragem de componentes;
- Extração de características;
- Comparação experimental;
- Registro de resultados quantitativos.

O escopo foi mantido: detecção candidata de rachaduras em paredes.

## 4. Dados

O conjunto experimental contém cinco imagens:

- Img1.png
- Img2.png
- Img3.png
- Img4.png
- Img5.png

As imagens estão armazenadas em `images/input/`.

A caracterização, origem, condições de aquisição e limitações estão documentadas em `docs/dataset.md`.

A avaliação atual é preliminar, pois ainda não existem máscaras de referência manual validadas.

## 5. Pipeline implementado

O pipeline executa as seguintes etapas:

1. Leitura da imagem;
2. Conversão para escala de cinza;
3. Suavização com filtro Gaussiano;
4. Detecção de bordas utilizando Canny;
5. Realce de estruturas escuras com black-hat;
6. Limiarização;
7. Fechamento morfológico;
8. Análise de componentes conectados;
9. Filtragem por área mínima;
10. Extração de características;
11. Geração de máscaras e sobreposições;
12. Registro dos resultados em CSV.

### 5.1 Canny

O Canny é mantido como baseline da M1.

Os parâmetros utilizados são:

- Limiar inferior: 50;
- Limiar superior: 150;
- Suavização Gaussiana: 5 × 5.

A saída é uma imagem binária de bordas.

### 5.2 Black-hat morfológico

O black-hat é utilizado para realçar estruturas escuras em relação ao entorno.

A operação corresponde à diferença entre o fechamento morfológico da imagem e a imagem original.

O elemento estruturante utilizado é elíptico, com dimensão 9 × 9.

A técnica é adequada como etapa de realce, mas pode destacar sombras, manchas e texturas.

### 5.3 Limiarização

Após o black-hat, é aplicada uma limiarização binária.

São utilizadas duas configurações:

| Configuração | Limiar |
|---|---:|
| A | 12 |
| B | 24 |

Todos os demais parâmetros permanecem constantes.

### 5.4 Fechamento morfológico

O fechamento morfológico utiliza um elemento estruturante elíptico de 3 × 3, com uma iteração.

Sua finalidade é conectar pequenos intervalos entre regiões candidatas.

### 5.5 Componentes conectados

A análise de componentes conectados identifica regiões independentes da máscara.

Para cada componente, são extraídos:

- Área em pixels;
- Coordenada X;
- Coordenada Y;
- Largura;
- Altura;
- Razão de aspecto.

A área é medida em pixels e não representa uma medida física.

A razão de aspecto é calculada pela divisão entre a maior e a menor dimensão da caixa delimitadora.

## 6. Experimento M2

### 6.1 Pergunta experimental

Como a alteração do limiar black-hat de 12 para 24 modifica a quantidade de pixels classificados como candidatos a rachadura?

### 6.2 Variáveis

Variável independente:

- Limiar black-hat.

Variáveis mantidas constantes:

- Imagens;
- Kernel black-hat;
- Área mínima;
- Fechamento morfológico;
- Procedimento de processamento.

### 6.3 Indicadores

São registrados:

- Quantidade de pixels candidatos;
- Fração de pixels candidatos;
- Número de componentes;
- Área do maior componente.

A fração de pixels candidatos é calculada por:

fração = pixels candidatos / total de pixels da imagem

Esses indicadores descrevem a saída do algoritmo.

Sem máscaras de referência, não representam precisão, revocação, IoU ou Dice.

### 6.4 Resultados

Os resultados completos estão em:

`images/results_m2/experiment_summary.csv`

A configuração B utiliza um limiar mais alto e tende a selecionar menos pixels do que a configuração A.

Essa redução pode representar a remoção de falsos positivos, mas também pode eliminar partes reais das rachaduras.

Portanto, a redução da quantidade de pixels não comprova, isoladamente, uma melhora na qualidade da segmentação.

### 6.5 Análise de casos

A análise visual deve considerar:

- Imagens em que as rachaduras apresentam contraste elevado;
- Imagens com iluminação irregular;
- Regiões com textura superficial;
- Rachaduras finas;
- Regiões em que o algoritmo destaca sombras ou manchas.

Os arquivos de sobreposição permitem comparar as regiões candidatas com a imagem original.

A equipe deverá registrar no vídeo pelo menos um caso de sucesso e uma limitação observada.

## 7. Limitações

O sistema apresenta as seguintes limitações:

- Conjunto de dados pequeno;
- Ausência de máscaras de referência validadas;
- Possibilidade de falsos positivos;
- Possibilidade de perda de rachaduras finas;
- Sensibilidade aos parâmetros;
- Ausência de avaliação quantitativa baseada em referência;
- Ausência de classificação final;
- Ausência de medida física da largura das rachaduras.

## 8. Plano de conclusão para a M3

| Tarefa | Evidência esperada |
|---|---|
| Confirmar origem e licença das imagens | Inventário atualizado |
| Produzir máscaras de referência | Máscaras revisadas |
| Calcular IoU, Dice, precisão e revocação | Tabela de métricas |
| Avaliar parâmetros em imagens reservadas | Comparação final |
| Revisar código e documentação | Repositório atualizado |
| Preparar apresentação final | Demonstração reproduzível |

## 9. Conclusão

A M2 representa uma evolução da implementação inicial da M1.

O sistema passou da detecção genérica de bordas para um fluxo de realce, segmentação, morfologia e análise de componentes conectados.

A comparação entre os limiares 12 e 24 permite observar como a alteração de um parâmetro modifica a saída.

A avaliação de qualidade permanece preliminar devido à ausência de máscaras de referência.

Na M3, o objetivo será validar a segmentação com referências manuais, calcular métricas de qualidade e avaliar o desempenho em imagens reservadas.

## 10. Declaração de uso de IA

Foi utilizada a ferramenta ChatGPT como apoio à organização da documentação, elaboração de código Python e estruturação dos experimentos.

Os materiais afetados incluem:

- `src/main.py`;
- `README.md`;
- `docs/dataset.md`;
- `docs/relatorio_m2.md`;
- `requirements.txt`.

A equipe deve executar, revisar e compreender os materiais antes da entrega.

## 11. Referências

OpenCV Documentation.  
https://docs.opencv.org/

GONZALEZ, R. C.; WOODS, R. E. Digital Image Processing. Pearson.

BRADSKI, G.; KAEHLER, A. Learning OpenCV: Computer Vision with the OpenCV Library. O'Reilly.