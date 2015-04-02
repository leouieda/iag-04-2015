# Fatiando a Terra: construindo uma base para ensino e pesquisa de geofísica

## Resumo

Geofísicos utilizam obervações indiretas para inferir a estrutura interna
e as propriedades físicas da Terra.

Isso é feito através de modelagem direta e inversão.

Modelagem direta é o processo de simular computacionalmente como os processos e
propriedades físicas da Terra produzem os fenômenos observados na superfície.

Inversão é o processo de estimar os parâmetros internos da Terra a partir das
observações.

Métodos de inversão utilizam a modelagem direta.

Muitas vezes a modelagem direta é o fator limitante da performance
computacional da inversão.

Métodos eficientes de modelagem direta são necessários para desenvolver
uma inversão eficiente.

A criação de novos algoritmos de modelagem direta e inversão requer o
desenvolvimento de programas de computador que implementem o novo método.

Esses programas são normalmente produzidos através da cópia de trechos do
código de diversos programas anteriores.

Infelizmente, muitas vezes esses códigos anteriores não estão disponíveis.

Pesquisadores fazem suas próprias implementações para poder usar métodos
publicados em seus próprios algoritmos.

Grande parte do código é destinado a tarefas auxiliares, como
ler e salvar dados e resultados em arquivos,
ler parâmetros de configuração do algoritmo,
produzir gráficos,
etc.

O fluxograma para produzir um resultado envolve diversos programas diferentes
que muitas vezes não utilizam os mesmo formatos de arquivo.

Essa repetição e falta de integração entre os componentes leva à baixa
produtividade do pesquisador e alto risco de erros no programa final.




O projeto Fatiando a Terra (fatiando.org) tem como objetivo facilitar o
trabalho de pesquisadores e professores na área geofísica.

O projeto é uma biblioteca feita na linguagem Python, que é conhecida pela
facilidade de ser aprendida e o grande número de bibliotecas científicas
disponível.

A biblioteca permite que os usuários integrem input/output de dados,
processamento, modelagem, inversão e visualização utilizando Python ao invés de
"shell scripts".

O Fatiando a Terra foi desenvolvido para facilitar a combinação de seus
componentes de diversas formas diferentes.

Por exemplo, o mesmo módulo de modelagem direta pode ser usado para produzir
dados sintéticos, desenvolver um método de inversão ou como parte de uma
interface gráfica interativa.

As possibilidades de combinação aumentam o crescimento da biblioteca,

Além disso, as funções da biblioteca podem ser combinadas funções desenvolvidas
pelo usuário e com as muitas
bibliotecas científicas da linguagem Python: visualização 2D e 3D, produção de
mapas, análise estatística, programação paralela, aplicativos para Internet,
etc.

O módulo de problemas inversos do Fatiando a Terra automatiza grande parte da
implementação de um novo método de inversão.

O pesquisar implementa somente o cálculo de dados preditos e da matriz de
sensibilidade utilizando os diversos módulos de modelagem direta.

Com a implementação dessas duas funções, o usuário pode escolher livremente
entre diversos métodos de optimização e regularização.



Para o ensino de geofísica, o Fatiando a Terra pode ser combinado com a
interatividade de outros programas, particularmente o IPython notebook
(ipython.org).

Conceitos difíceis de serem transmitidos em aula podem ser explorados pelos
alunos de forma interativa, com gráficos e animações.

Por exemplo, os alunos podem explorar como o campo geomagnético interage com um
corpo geológico para produzir uma anomalia magnética de campo total.

Para ensinar a reflexão e refração de ondas sísmicas, o professor pode
utilizar simulações numéricas da propagação de ondas para produzir animações em
tempo real.



A implementação de diversos métodos geofísicos em uma única biblioteca
fornece a base necessária para a rápida criação de novas metodologias e
material didático interativo.

Eu e os demais membros do Grupo de Problemas Inversos em Geofísica
(www.pinga-lab.org) utilizamos o Fatiando a Terra em nossa pesquisa e ensino.

Os métodos desenvolvidos pelo grupo são incluídos na biblioteca junto com a
publicação de artigos.

Essa disponibilidade encoraja a reutilização desses métodos e promove a
abertura do processo científico.

A maior parte da funcionalidade atual é para gravimetria e magnetometria,
embora já exista um núcleo de sísmica e sismologia que está sendo desenvolvido.

O projeto precisa de usuários e desenvolvedores para crescer e abranger os
demais ramos da geofísica.

O projeto é software livre e contribuições de qualquer forma são bem vindas.
