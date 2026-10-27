# Revisão da M1 e Plano de Ação para a M2

## 1. Parte A — Identificação da equipe e dos materiais conferidos

| Item | Informação |
|---|---|
| Identificação do grupo | Grupo 15 |
| Integrantes | Gustavo Koerich Cardoso; Iago Fermiano Orsi; Igor Orsi Dalagnello |
| Projeto | Detecção de rachaduras em paredes |
| Repositório avaliado | https://github.com/Igororsi/detecao-rachaduras-paredes |
| Commit, versão ou estado da entrega M1 | `d577fdb6475c53859d65c3aaf869d368a893d2cc` |
| Documento de feedback consultado | Devolutiva da M1 — Grupo 15 |
| Data da conferência | 15/09/2026 |
| Nota informada na devolutiva | 73,75 após o vídeo, conforme a devolutiva recebida |
| Nota registrada no diário | 7,4 |

A conferência foi realizada com base na devolutiva fornecida pelo docente e na identificação do commit avaliado indicada no próprio feedback.

## 2. Parte B — Resposta ao feedback

| Nº | Síntese da observação recebida | Classificação do grupo | Evidência ou justificativa | Ação decorrente |
|---:|---|---|---|---|
| 1 | A localização de rachaduras está clara, mas as informações úteis e os tipos de superfície estão amplos. | Concordamos parcialmente | O problema de detecção de rachaduras foi definido, mas o feedback indica que ainda é necessário delimitar melhor as superfícies e os tipos de situações analisadas. | Refinar a delimitação do problema e registrar explicitamente tipos de parede, texturas e condições que serão consideradas na M2. |
| 2 | Existem cinco imagens, porém a origem/licença de cada arquivo e a representatividade do conjunto são insuficientes. | Concordamos | O feedback reconhece a existência das cinco imagens, mas aponta falta de associação entre cada arquivo e sua proveniência. | Registrar a origem e a licença de cada imagem e ampliar o conjunto com fotos próprias, imagens públicas devidamente identificadas e imagens geradas claramente separadas. |
| 3 | Há entrada e saída, mas não existem métrica nem definição operacional de rachadura. | Concordamos | O baseline mostra resultados, porém não há critérios quantitativos nem verdade de referência suficientes para medir o desempenho. | Criar máscaras de referência/anotações de regiões, definir o que será considerado rachadura e adotar métricas objetivas. |
| 4 | O pipeline é coerente e possui critérios geométricos iniciais. | Concordamos | O feedback considera a sequência inicial adequada, mas orienta que ela seja ampliada para não tratar o mapa de bordas como resultado final. | Evoluir o pipeline com segmentação, filtragem geométrica, análise de componentes e comparação entre etapas. |
| 5 | O baseline em Canny demonstra teste real e evidencia muitos falsos positivos. | Concordamos | O próprio experimento mostrou que Canny detecta muitas bordas que não correspondem a rachaduras. | Usar os falsos positivos observados para definir a próxima etapa de filtragem e projetar experimentos específicos para texturas difíceis. |
| 6 | O repositório possui código, dependências, entradas, resultados e comandos. | Concordamos | A devolutiva classificou o repositório como adequado. | Manter a organização e atualizar a documentação e os resultados conforme a evolução da M2. |
| 7 | A documentação é compreensível, mas repete conteúdo e precisa de evidências/citações mais precisas. | Concordamos | A estrutura documental atende ao básico, mas ainda pode ficar mais objetiva e rastreável. | Revisar o Markdown, reduzir repetições e associar afirmações e resultados às respectivas imagens, experimentos e fontes. |
| 8 | O vídeo está acessível e possui aproximadamente 7min42s; conteúdo e participação ainda dependem de conferência docente. | Concordamos | O feedback informa que acesso e duração foram confirmados, mas o conteúdo ainda estava pendente de conferência. | Manter o vídeo como evidência da etapa M1 e registrar eventuais ajustes conforme orientação docente. |
| 9 | Há vários commits e registros de participação de integrantes. | Concordamos | O histórico foi considerado adequado na devolutiva. | Manter o histórico de commits e distribuir as novas atividades da M2 entre os integrantes. |

### 2.1 Síntese da posição do grupo

O grupo compreendeu e aceita a maior parte dos pontos da avaliação, principalmente os relacionados à necessidade de melhorar a documentação do conjunto de imagens, definir uma verdade de referência e adotar métricas quantitativas. Também foi compreendido que o resultado do Canny deve ser tratado como baseline e não como detecção final, pois os próprios experimentos demonstraram muitos falsos positivos.

Os pontos que exigem aprofundamento estão relacionados principalmente à delimitação do problema, à representatividade dos dados, à documentação da origem/licença das imagens e à definição de critérios objetivos para medir o desempenho. A crítica com maior impacto técnico sobre a continuidade do projeto é a ausência de referência anotada e de métricas, pois sem isso fica difícil comparar de forma objetiva diferentes configurações do pipeline na M2.

## 3. Parte C — Conferência das pontuações

A devolutiva apresenta os seguintes critérios e pontuações:

| Critério | Valor máximo | Nível atribuído | Pontuação registrada | Pontuação recalculada pelo grupo | Diferença |
|---|---:|---|---:|---:|---:|
| 1. Problema | 15,00 | Adequado | 11,25 | 11,25 | 0,00 |
| 2. Imagens e dados | 10,00 | Parcial | 5,00 | 5,00 | 0,00 |
| 3. Objetivos e sucesso | 10,00 | Parcial | 5,00 | 5,00 | 0,00 |
| 4. Pipeline | 15,00 | Adequado | 11,25 | 11,25 | 0,00 |
| 5. Viabilidade | 15,00 | Adequado | 11,25 | 11,25 | 0,00 |
| 6. Repositório | 10,00 | Adequado | 7,50 | 7,50 | 0,00 |
| 7. Markdown | 10,00 | Adequado | 7,50 | 7,50 | 0,00 |
| 8. Vídeo | 10,00 | Pendente / após vídeo | 10,00 | 10,00 | 0,00 |
| 9. Histórico | 5,00 | Adequado | 3,75 | 3,75 | 0,00 |
| **Total da tabela** | **100,00** |  | **72,50** | **72,50** | **0,00** |

### 3.1 Memória de cálculo

A soma dos valores apresentados na tabela da devolutiva é:

```text
11,25 + 5,00 + 5,00 + 11,25 + 11,25 + 7,50 + 7,50 + 10,00 + 3,75 = 72,50
```

O subtotal indicado na própria devolutiva como verificável, antes da consideração do vídeo, é de **62,50/90**, o que coincide com a soma dos oito primeiros critérios antes do vídeo:

```text
11,25 + 5,00 + 5,00 + 11,25 + 11,25 + 7,50 + 7,50 + 3,75 = 62,50
```

Entretanto, a devolutiva informa **73,75 pontos após o vídeo**, enquanto a soma dos valores explicitamente exibidos na tabela resulta em **72,50**. Existe, portanto, uma diferença de **1,25 ponto** entre a soma dos valores apresentados e o total final informado.

### 3.2 Resultado da conferência aritmética

- [ ] A soma está correta e coincide com a nota da devolutiva.
- [x] Foi identificada uma possível divergência na soma.
- [ ] Não foi possível reproduzir a soma.

**Explicação:** a soma dos critérios apresentados resulta em 72,50 pontos, enquanto o total final informado na devolutiva é 73,75 pontos. O grupo registra a divergência de 1,25 ponto para esclarecimento, sem afirmar previamente qual valor deve prevalecer.

## 4. Parte D — Conferência da nota registrada no diário

| Verificação | Valor |
|---|---:|
| Nota recalculada a partir da ficha | 72,50/100, conforme os valores exibidos na tabela |
| Nota apresentada na devolutiva | 73,75/100 após o vídeo |
| Nota registrada no diário | 7,4 |
| Diferença identificada | Há diferença entre a soma da tabela (72,50), o total informado na devolutiva (73,75) e a nota exibida no diário (7,4) |

- [ ] A nota registrada no diário está correta.
- [x] A nota registrada no diário parece diferente da nota da devolutiva.
- [ ] O grupo ainda não conseguiu consultar ou confirmar o registro.

**Observação:** a nota do diário informada pelo grupo é **7,4**. A conversão direta de 73,75/100 para uma escala de 0 a 10 resultaria em 7,375, que pode ser apresentada como 7,4 dependendo da regra de arredondamento adotada. Como a ficha exibida na devolutiva soma 72,50, permanece a necessidade de esclarecer a diferença de 1,25 ponto entre a soma da tabela e os 73,75 informados no fechamento.

## 5. Parte E — Diagnóstico da situação atual

| Componente | Situação atual | Evidência existente | Lacuna identificada |
|---|---|---|---|
| Definição e delimitação do problema | Parcial | Projeto define detecção de rachaduras em paredes | Delimitar melhor tipos de superfície e condições. |
| Objetivo e saída esperada | Parcial | Há entrada e saída do pipeline | Definir operacionalmente o que é rachadura e como o resultado será medido. |
| Conjunto inicial de imagens | Parcial | Cinco imagens utilizadas no baseline | Associar cada arquivo à origem/licença e ampliar diversidade. |
| Pipeline proposto | Adequado | Baseline com Canny e critérios geométricos iniciais | Evoluir para segmentação, filtragem, componentes e análise quantitativa. |
| Evidência de viabilidade | Adequado | Execução do baseline em cinco imagens | Medir desempenho com referência e métricas. |
| Fundamentação e referências | Parcial | Documentação existente | Melhorar citações e rastreabilidade das fontes. |
| Organização do repositório | Adequado | Código, dependências, entradas, resultados e comandos | Manter organização e atualizar conforme a M2. |
| Relatório técnico | Parcial | Resultados e observações da M1 | Incluir evidências quantitativas, limitações e comparação entre configurações. |
| Página parcial do projeto | Parcial | Material do projeto já existente | Atualizar com resultados da M2 e comparação visual/quantitativa. |
| Registro de decisões e limitações | Parcial | Feedback registra que Canny gera muitos falsos positivos | Documentar decisões, parâmetros, casos difíceis e limitações ao longo da M2. |

## 6. Parte F — Plano de ação para a M2

### 6.1 Ajustes herdados da M1

| Prioridade | Problema identificado na M1 | Ação de correção | Responsável | Prazo | Evidência de conclusão |
|---|---|---|---|---|---|
| Essencial | Origem e licença das imagens não estão associadas individualmente aos arquivos | Criar tabela com nome do arquivo, origem, tipo e licença/crédito | Gustavo | 25/09/2026 | Tabela no repositório e documentação atualizada |
| Essencial | Ausência de verdade de referência e critérios quantitativos | Criar anotações/máscaras de referência para um pequeno conjunto com e sem rachaduras | Iago | 30/09/2026 | Máscaras e conjunto de referência no repositório |
| Essencial | Canny produz muitos falsos positivos | Usar os falsos positivos observados para definir filtros e etapas adicionais do pipeline | Igor | 30/09/2026 | Comparação do baseline com pipeline aprimorado |
| Importante | Conjunto pouco representativo | Adicionar paredes sem rachadura, texturas difíceis e situações variadas | Gustavo | 05/10/2026 | Novas imagens com origem documentada |
| Importante | Documentação repete conteúdo e possui citações pouco precisas | Revisar README/relatório e associar resultados às evidências | Iago | 10/10/2026 | Markdown atualizado e referências rastreáveis |
| Recomendável | Critérios geométricos ainda precisam de calibração | Registrar parâmetros, justificativas e limitações dos filtros | Igor | 15/10/2026 | Tabela de parâmetros e análise de erros |

### 6.2 Novos desenvolvimentos da M2

| Entrega ou resultado da M2 | Tarefa concreta | Responsável principal | Colaboradores | Prazo | Evidência esperada | Dependências ou riscos |
|---|---|---|---|---|---|---|
| Implementação inicial executável | Organizar uma execução reprodutível do pipeline completo | Gustavo | Iago, Igor | 25/09/2026 | Comando documentado e execução registrada | Dependências do ambiente |
| Segmentação | Implementar e testar a etapa de segmentação de regiões candidatas | Gustavo | Iago | 30/09/2026 | Imagem de máscara/resultado e parâmetros | Iluminação e textura da parede |
| Morfologia matemática | Aplicar operações morfológicas para reduzir ruído e conectar/regulamentar regiões candidatas | Gustavo | Igor | 30/09/2026 | Comparação antes/depois e justificativa | Escolha de kernel e número de operações |
| Extração de características | Extrair características relevantes de cor, forma, textura ou estrutura | Iago | Igor | 05/10/2026 | Tabela, CSV ou registro dos descritores | Características podem não separar todos os casos |
| Experimentos com parâmetros | Comparar configurações sob o mesmo conjunto e protocolo | Iago | Gustavo, Igor | 10/10/2026 | Configurações comparadas | Comparabilidade dos experimentos |
| Testes e casos difíceis | Testar imagens com e sem rachaduras, texturas difíceis e falsos positivos observados no baseline | Igor | Gustavo, Iago | 10/10/2026 | Imagens, resultados e análise dos erros | Conjunto ainda pequeno |
| Relatório técnico parcial | Atualizar métodos, parâmetros, resultados e limitações | Iago | Gustavo, Igor | 15/10/2026 | Relatório atualizado | Necessidade de resultados produzidos antes do fechamento |
| Página parcial | Atualizar a apresentação do projeto com comparação visual e quantitativa | Igor | Gustavo, Iago | 15/10/2026 | Estado atual, comparação visual e próximos passos | Sincronização com resultados finais da etapa |
| Organização e reprodutibilidade | Atualizar README, dependências, comandos, fontes e licenças | Gustavo | Iago, Igor | 15/10/2026 | README e estrutura do repositório atualizados | Mudanças simultâneas no pipeline |

### 6.3 Protocolo experimental mínimo

| Elemento | Definição do grupo |
|---|---|
| Pergunta do experimento | Como melhorar a separação de rachaduras em relação ao baseline baseado em bordas? |
| Imagens ou amostra utilizadas | Conjunto ampliado com imagens com rachaduras, sem rachaduras e texturas difíceis, mantendo a origem documentada. |
| Método principal | Pipeline com segmentação, operações morfológicas, filtragem geométrica, análise de componentes e extração de características. |
| Configurações ou parâmetros comparados | Parâmetros de segmentação, kernels/iterações morfológicas e critérios geométricos, mantendo as demais condições controladas quando possível. |
| Resultado esperado | Redução de falsos positivos e melhor correspondência entre regiões detectadas e regiões anotadas como rachadura. |
| Métrica ou critério de comparação | Precisão, revocação e IoU das regiões em comparação com as máscaras de referência. |
| Forma de registrar os resultados | Tabela por imagem e por configuração, acompanhada das imagens de saída e dos parâmetros utilizados. |
| Limitações já previstas | Variação de iluminação, textura, cor da parede, tamanho e orientação das rachaduras e possíveis confusões com outras estruturas lineares. |

### 6.4 Distribuição das responsabilidades

| Integrante | Responsabilidades principais | Artefatos ou partes sob sua responsabilidade | Como o trabalho será validado pelo grupo |
|---|---|---|---|
| Gustavo Koerich Cardoso | Segmentação, morfologia e organização da execução | Código da segmentação/morfologia, comandos de execução e documentação das dependências | Testes em conjunto e revisão dos resultados pelos três integrantes |
| Iago Fermiano Orsi | Extração de características, testes e apoio à análise | Descritores, tabelas de resultados e atualização do relatório técnico | Conferência cruzada dos resultados e comparação com as máscaras de referência |
| Igor Orsi Dalagnello | Métricas, experimentos e documentação da análise | Cálculo das métricas, comparação de parâmetros e registro das limitações | Repetição dos experimentos e conferência dos resultados pelo grupo |

## 7. Parte G — Compromisso da equipe

Declaramos que revisamos a devolutiva da M1, conferimos as pontuações e a nota registrada no diário, identificamos as correções necessárias e definimos um plano de ação para a M2. A possível divergência aritmética identificada foi registrada de forma objetiva para esclarecimento. As observações do feedback foram convertidas em ações verificáveis e os integrantes conhecem as tarefas, os prazos e os resultados esperados para a próxima etapa.

**Integrantes:**

- Gustavo Koerich Cardoso
- Iago Fermiano Orsi
- Igor Orsi Dalagnello

**Data:** 15/09/2026

## 8. Checklist antes da entrega

- [x] Identificou corretamente a equipe e a entrega avaliada.
- [x] Respondeu às observações relevantes do feedback.
- [x] Diferenciou concordância, concordância parcial e discordância.
- [x] Registrou a divergência de pontuação com memória de cálculo.
- [x] Comparou a nota calculada, a nota da devolutiva e a nota do diário.
- [x] Separou correções herdadas da M1 e novos desenvolvimentos da M2.
- [x] Definiu tarefas, responsáveis, prazos e evidências de conclusão.
- [x] Incluiu segmentação, morfologia, extração de características e experimentação no plano da M2.
- [x] Definiu um protocolo experimental mínimo.
- [x] Registrou dependências, riscos e limitações.
- [x] Registrou responsabilidades dos integrantes.
