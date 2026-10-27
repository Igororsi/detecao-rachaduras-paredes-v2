# Proposta do Projeto

## Título

Sistema de Detecção de Rachaduras em Paredes Utilizando Processamento Digital de Imagens

---

# 1. Problema

A identificação de rachaduras em paredes é uma atividade importante para a manutenção e avaliação de estruturas civis.

Normalmente essa tarefa é realizada por inspeção visual humana, exigindo tempo e atenção dos responsáveis pela análise.

Este projeto pretende investigar como técnicas de Processamento Digital de Imagens podem ser utilizadas para detectar automaticamente rachaduras em fotografias de paredes.

A informação que se deseja obter é a localização das regiões que apresentam possíveis rachaduras, permitindo destacar essas áreas para posterior análise.

---

# 2. Contexto de Aplicação

A solução poderá ser utilizada em atividades relacionadas à construção civil e manutenção predial.

Entre os possíveis cenários de aplicação estão:

- Inspeção de imóveis;
- Avaliação de edificações;
- Monitoramento de estruturas;
- Manutenção preventiva;
- Apoio à identificação de danos estruturais.

Embora o projeto possua caráter acadêmico, o problema tratado possui relevância prática e aplicação real.

---

# 3. Objetivo

## Objetivo Geral

Desenvolver um sistema capaz de detectar rachaduras em imagens de paredes utilizando técnicas de processamento digital de imagens.

## Objetivos Específicos

- Obter um conjunto representativo de imagens;
- Estudar métodos de pré-processamento;
- Aplicar filtros para redução de ruído;
- Implementar técnicas de detecção de bordas;
- Avaliar métodos de segmentação;
- Destacar automaticamente rachaduras;
- Comparar os resultados obtidos.

---

# 4. Entrada e Saída Esperadas

## Entrada

Imagens digitais contendo superfícies de paredes.

Exemplos:

- Paredes internas;
- Paredes externas;
- Superfícies com rachaduras;
- Superfícies sem rachaduras.

## Saída

Imagem processada contendo:

- Regiões destacadas;
- Indicação visual das rachaduras detectadas;
- Informações relacionadas às áreas identificadas.

---

# 5. Conjunto de Dados

O conjunto inicial de imagens será composto por fotografias contendo paredes com e sem rachaduras.

## Origem das imagens

- Bases públicas de pesquisa;
- Bancos de imagens gratuitos;
- Fotografias produzidas pelos integrantes.

## Quantidade inicial

Para o experimento preliminar da M1 foram utilizadas 5 imagens de entrada.

Nas próximas etapas, o conjunto de imagens será ampliado para permitir uma avaliação mais abrangente do método.

## Formatos

- JPG
- JPEG
- PNG

## Resolução

Variável, dependendo da origem das imagens.

---

# 6. Pipeline Preliminar

```text
Imagem Original
        ↓
Conversão para Escala de Cinza
        ↓
Redução de Ruído
        ↓
Detecção de Bordas
        ↓
Operações Morfológicas
        ↓
Identificação das Regiões
        ↓
Resultado Final
```

---

## Etapa 1 – Conversão para Escala de Cinza

Objetivo:

Reduzir a complexidade da imagem removendo informações de cor que não são essenciais para a detecção de rachaduras.

---

## Etapa 2 – Redução de Ruído

Objetivo:

Remover pequenas variações e imperfeições presentes na imagem.

Técnicas consideradas:

- Gaussian Blur;
- Median Blur.

---

## Etapa 3 – Detecção de Bordas

Objetivo:

Destacar regiões onde há mudanças bruscas de intensidade.

Técnicas consideradas:

- Canny Edge Detection;
- Sobel.

---

## Etapa 4 – Operações Morfológicas

Objetivo:

Conectar regiões relevantes e eliminar pequenos artefatos.

Técnicas consideradas:

- Dilatação;
- Erosão;
- Closing.

---

## Etapa 5 – Identificação das Rachaduras

Objetivo:

Selecionar estruturas que apresentem características compatíveis com rachaduras.

Critérios iniciais:

- Comprimento;
- Espessura;
- Continuidade;
- Formato irregular.

---

# 7. Arquitetura Preliminar

```text
Usuário
   ↓
Imagem de Entrada
   ↓
Módulo de Pré-Processamento
   ↓
Módulo de Detecção
   ↓
Módulo de Análise
   ↓
Resultado
```

---

# 8. Estudo Inicial de Viabilidade

A viabilidade do projeto é sustentada pelos seguintes fatores:

- Existência de bibliotecas consolidadas para PDI;
- Disponibilidade de imagens públicas;
- Grande quantidade de material acadêmico relacionado;
- Facilidade de implementação dos métodos iniciais;
- Possibilidade de evolução gradual durante as próximas etapas do projeto.

A biblioteca OpenCV fornece recursos suficientes para a implementação inicial do sistema.

---

# 9. Experimentos Preliminares

Foi realizado um experimento preliminar utilizando a biblioteca OpenCV para verificar a viabilidade da abordagem proposta.

O experimento foi aplicado às cinco imagens disponíveis na pasta `images/input/` e seguiu as seguintes etapas:

1. Leitura das imagens;
2. Conversão para escala de cinza;
3. Aplicação de filtro Gaussiano para redução de ruído;
4. Detecção de bordas utilizando o algoritmo Canny;
5. Salvamento dos resultados processados na pasta `images/results/`;
6. Comparação visual entre as imagens de entrada e os resultados.

Os resultados obtidos demonstram que a detecção de bordas é capaz de destacar diferentes características presentes nas superfícies analisadas, incluindo regiões correspondentes a possíveis rachaduras.

Entretanto, também são identificadas outras bordas relacionadas à textura da parede, iluminação e demais características das imagens. Dessa forma, o experimento indica a viabilidade da abordagem, mas evidencia a necessidade de técnicas adicionais para reduzir falsos positivos e melhorar a identificação das regiões de interesse.

Os resultados deste experimento serão utilizados como base para o refinamento do pipeline nas próximas etapas do projeto.

---

# 10. Origem das Imagens

As imagens utilizadas no projeto foram obtidas das seguintes fontes:

1. Imagens produzidas pelos integrantes do grupo por meio de fotografias de paredes com rachaduras.

2. Imagens geradas com auxílio de Inteligência Artificial para fins de teste e validação preliminar do pipeline de processamento.

3. Bases públicas de imagens quando aplicável.

As imagens utilizadas encontram-se armazenadas na pasta:

images/input/

---

# 11. Uso de Inteligência Artificial Generativa

Durante o desenvolvimento da primeira parte do projeto foi utilizada a ferramenta ChatGPT (OpenAI) para auxiliar na elaboração inicial de textos da documentação, organização da proposta e sugestões de estrutura do projeto.

Todo o conteúdo gerado foi revisado pelos integrantes do grupo, que permaneceram responsáveis pela validação das informações, decisões técnicas e adequação do material entregue.

A utilização da ferramenta teve caráter de apoio à redação e organização da documentação, não substituindo a análise técnica realizada pelos integrantes.

---

# 12. Próximos Passos (M2)

- Expandir o conjunto de imagens;
- Refinar o pipeline;
- Ajustar parâmetros dos filtros;
- Avaliar novas técnicas de segmentação;
- Desenvolver métricas de avaliação;
- Melhorar a precisão da detecção.

---

# 13. Referências

OpenCV Documentation. Disponível em: https://opencv.org/

OpenCV Python Tutorials. Disponível em: https://docs.opencv.org/

Bradski, G.; Kaehler, A. Learning OpenCV: Computer Vision with the OpenCV Library.

Gonzalez, R. C.; Woods, R. E. Processamento Digital de Imagens.

Documentação NumPy. Disponível em: https://numpy.org/

## Experimento preliminar

Foi realizado um experimento preliminar utilizando a biblioteca OpenCV com o objetivo de verificar a viabilidade da detecção de características semelhantes a rachaduras nas imagens.

O processamento utilizado consiste inicialmente na conversão das imagens para escala de cinza, seguida pela aplicação de um filtro Gaussiano para redução de ruídos e, posteriormente, pela detecção de bordas utilizando o algoritmo Canny.

Foram processadas cinco imagens de entrada, armazenadas em `images/input/`. Os resultados do processamento foram armazenados em `images/results/`.

O experimento permitiu observar as bordas presentes nas imagens, incluindo regiões correspondentes a possíveis rachaduras. Também foram identificadas outras bordas provenientes da textura da parede, iluminação e demais características presentes nas imagens.

Dessa forma, o experimento preliminar indica que a abordagem possui potencial para destacar características relacionadas às rachaduras. Entretanto, ainda são necessárias etapas adicionais de processamento e análise para reduzir falsos positivos e melhorar a identificação das regiões de interesse.
