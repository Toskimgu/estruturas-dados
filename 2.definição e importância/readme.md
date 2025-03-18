## 2. Definição e Importância das Estruturas de Dados no Desenvolvimento de Programas

# Definição e Importância das Estruturas de Dados no Desenvolvimento de Programas

## Estruturas de Dados Lineares vs. Não Lineares

### Estruturas Lineares

As **estruturas de dados lineares** são aquelas onde os elementos são organizados de forma sequencial. Cada elemento tem exatamente um predecessor (exceto o primeiro) e um sucessor (exceto o último). As operações em estruturas lineares geralmente envolvem a inserção, remoção e acesso aos elementos de maneira sequencial.

#### Exemplos de Estruturas Lineares:
- **Listas**: Um conjunto de elementos organizados sequencialmente, onde os elementos podem ser acessados por índices.
- **Filas**: Uma estrutura de dados onde o primeiro elemento inserido é o primeiro a ser removido (FIFO - First In, First Out).
- **Pilhas**: Onde o último elemento inserido é o primeiro a ser removido (LIFO - Last In, First Out).

### Estruturas Não Lineares

As **estruturas de dados não lineares** são aquelas onde os elementos não têm uma organização sequencial única. Em vez disso, eles são organizados de maneira hierárquica ou em rede, onde cada elemento pode ter múltiplos predecessores e sucessores.

#### Exemplos de Estruturas Não Lineares:
- **Árvores**: Estruturas hierárquicas, onde cada elemento (nó) pode ter zero ou mais filhos.
- **Grafos**: Conjunto de nós conectados por arestas, onde não há uma estrutura sequencial fixa.

### Impacto no Desempenho

A escolha da estrutura de dados correta pode impactar significativamente o desempenho de um programa. Por exemplo:

- **Estruturas Lineares** são mais simples e diretas para muitos problemas, mas não são ideais para casos em que o acesso rápido a elementos não sequenciais é necessário.
- **Estruturas Não Lineares** são mais complexas e geralmente mais poderosas, pois permitem representar relações complexas entre dados, mas podem ter operações mais caras em termos de tempo e memória.

A escolha de qual estrutura usar depende dos requisitos do problema e da eficiência desejada. Vamos ver um exemplo prático de como uma estrutura de dados inadequada pode afetar o desempenho de um programa.

## Exemplo de Impacto no Desempenho

Em alguns casos, o uso de uma estrutura de dados inadequada pode resultar em um desempenho inferior, como mostrado no exemplo a seguir:

### Código sem estrutura de dados adequada

Imagine que estamos tentando ordenar uma lista de números, mas estamos utilizando uma abordagem ineficiente sem considerar a escolha adequada de uma estrutura.

```python
# Código ineficiente
numeros = [5, 2, 9, 1, 5, 6]

for i in range(len(numeros)):
    for j in range(len(numeros)):
        if numeros[i] < numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print("Lista ordenada sem estrutura eficiente:", numeros)
