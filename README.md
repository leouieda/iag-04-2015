# Fatiando a Terra: construindo uma base para ensino e pesquisa de geofísica

## Resumo

Geofísicos utilizam obervações indiretas para inferir a estrutura interna da
Terra. Esse processo é feito através de técnicas como modelagem direta e
inversão. A criação de novos algoritmos de modelagem direta e inversão requer o
desenvolvimento de programas de computador que implementem o novo método. Esses
programas são normalmente produzidos através da cópia de trechos do código de
diversos programas anteriores. Infelizmente, muitas vezes esses códigos não
estão disponíveis ou não podem ser facilmente reutilizados. Nesses casos, cada
pesquisador é obrigado a fazer suas próprias implementações e modificações.
Essa repetição e falta de integração entre os componentes leva à baixa
produtividade do pesquisador e alto risco de erros no programa final.

O Fatiando a Terra (www.fatiando.org) é uma biblioteca feita na linguagem
Python que tem como objetivo facilitar o trabalho de pesquisadores e
professores na área geofísica. Os módulos da biblioteca foram planejados para
facilitar a combinação de seus componentes de diversas formas. Por exemplo, o
mesmo módulo de modelagem direta pode ser usado para produzir dados sintéticos,
desenvolver um método de inversão ou como parte de uma interface gráfica
interativa. Além disso, as funções da biblioteca podem ser combinadas com
funções desenvolvidas pelo usuário e com as muitas bibliotecas científicas da
linguagem Python. O módulo de problemas inversos automatiza grande parte da
implementação de um novo método de inversão. O pesquisar implementa somente o
cálculo de dados preditos e da matriz de sensibilidade, ambos reutilizando os
diversos módulos de modelagem direta. Com essas duas funções, o usuário pode
escolher livremente entre diversos métodos de optimização e regularização para
executar sua inversão.

Para o ensino de geofísica, o Fatiando a Terra pode ser combinado com a
interatividade de outros programas, particularmente o IPython notebook
(www.ipython.org). Conceitos difíceis de serem transmitidos em aula podem ser
explorados pelos alunos de forma interativa, com botões, gráficos e animações.
Por exemplo, para ensinar a reflexão e refração de ondas sísmicas, o professor
pode utilizar simulações numéricas da propagação de ondas para produzir
animações em tempo real. Outro exemplo é permitir aos alunos explorar como o
campo geomagnético interage com um corpo geológico a diferentes latitudes para
produzir uma anomalia magnética de campo total. Dessa forma, os alunos ganham
experiência e intuição ao interagir com os resultados.

A implementação de diversos métodos geofísicos em uma única biblioteca fornece
a base necessária para a rápida criação de novas metodologias e material
didático interativo. A maior parte da funcionalidade atual é para gravimetria e
magnetometria, embora já exista um núcleo de sísmica e sismologia que está
sendo desenvolvido. O projeto necessita de usuários e desenvolvedores para
crescer e abranger os demais ramos da geofísica. O projeto é software livre e
contribuições de qualquer forma são bem vindas.
