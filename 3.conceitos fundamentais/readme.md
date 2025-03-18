## 3. Conceitos Fundamentais: Variáveis, Tipos de Dados e Alocação de Memória



## Variáveis e Tipos de Dados

### Variáveis
As **variáveis** são espaços de memória que armazenam valores. Elas permitem que você armazene e manipule dados durante a execução de um programa. Cada variável possui um nome e um tipo de dado associado, que define o tipo de valor que ela pode armazenar, como números, textos, ou outros objetos.

### Tipos de Dados
Os **tipos de dados** são categorias que definem o tipo de valor que uma variável pode armazenar. Alguns tipos comuns incluem:

- **Inteiros (int)**: Armazenam números inteiros, sem casas decimais (ex: `5`, `100`).
- **Ponto flutuante (float)**: Armazenam números com casas decimais (ex: `3.14`, `0.001`).
- **Strings (str)**: Armazenam texto, ou sequência de caracteres (ex: `"Olá"`, `"Python"`).
- **Booleanos (bool)**: Armazenam valores de verdadeiro ou falso (`True` ou `False`).
- **Listas (list)**: Coleções de valores ordenados, que podem ser de tipos diferentes (ex: `[1, 2, 3]`).
  
A escolha do tipo de dado afeta a forma como a memória é alocada para a variável.

## Alocação de Memória

A **alocação de memória** é o processo de reservar espaço na memória para armazenar variáveis e outros dados. Existem dois tipos principais de alocação de memória:

1. **Alocação Estática**: A memória é alocada em tempo de compilação e tem um tamanho fixo, ou seja, o tamanho não pode ser alterado durante a execução do programa.
2. **Alocação Dinâmica**: A memória é alocada em tempo de execução e pode ser ajustada conforme necessário. Isso permite a criação de estruturas de dados que podem crescer ou encolher durante a execução do programa.

### Diferença entre Alocação Estática e Dinâmica

- **Alocação Estática**: O tamanho da estrutura de dados é definido no momento da compilação. A memória é alocada uma única vez e permanece fixada durante a execução do programa. Exemplos típicos de alocação estática incluem arrays em muitas linguagens.
  
- **Alocação Dinâmica**: O tamanho da estrutura de dados é determinado durante a execução do programa, permitindo que ela cresça ou encolha conforme necessário. Exemplos típicos incluem listas e objetos em linguagens como Python, ou o uso de ponteiros em C/C++.

Nos exemplos a seguir, veremos a diferença entre esses dois tipos de alocação.


