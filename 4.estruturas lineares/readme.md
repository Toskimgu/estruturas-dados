## 4. Visão Geral das Estruturas Lineares

# Estruturas Lineares: Listas, Pilhas e Filas

As **estruturas lineares** são aquelas em que os elementos são armazenados de forma sequencial, ou seja, um elemento está conectado a outro, formando uma linha. Elas são fundamentais para a organização e manipulação de dados de forma eficiente em muitos tipos de programas. Neste documento, exploraremos três das principais estruturas lineares: **Listas**, **Pilhas** e **Filas**.

---

## 1. Listas

Uma **lista** é uma coleção de elementos organizados de forma sequencial. Em uma lista, cada elemento ocupa uma posição específica e pode ser acessado por um índice. As listas podem ser dinâmicas, permitindo o aumento ou diminuição de seu tamanho durante a execução do programa.

### Características:
- A lista permite acessar, inserir e remover elementos de qualquer posição.
- Em algumas linguagens, como Python, as listas podem conter diferentes tipos de dados, o que torna a estrutura bastante flexível.
- O acesso aos elementos é feito por meio de índices, sendo possível acessar qualquer elemento de maneira eficiente (O(1)).

### Operações principais:
- **Inserção**: Adicionar um elemento ao final ou em uma posição específica.
- **Remoção**: Remover um elemento de uma posição específica.
- **Acesso**: Obter o valor de um elemento dado seu índice.
- **Busca**: Encontrar um elemento em uma lista.

---

## 2. Pilhas

Uma **pilha** é uma estrutura de dados que segue o princípio **LIFO (Last In, First Out)**, ou seja, o último elemento inserido é o primeiro a ser removido. A pilha pode ser comparada a uma pilha de pratos, onde o último prato colocado é o primeiro a ser retirado.

### Características:
- Na pilha, os elementos são inseridos e removidos do mesmo lado, denominado "topo" da pilha.
- A pilha é ideal para problemas que exigem a reversão de uma sequência ou para controle de chamadas de funções recursivas, como em algoritmos de busca em profundidade.
  
### Operações principais:
- **Empilhar (push)**: Inserir um elemento no topo da pilha.
- **Desempilhar (pop)**: Remover o elemento do topo da pilha.
- **Verificar o topo (peek)**: Acessar o elemento no topo da pilha sem removê-lo.
- **Verificar se está vazia (is_empty)**: Verificar se a pilha não contém elementos.

---

## 3. Filas

Uma **fila** segue o princípio **FIFO (First In, First Out)**, ou seja, o primeiro elemento a ser inserido será o primeiro a ser removido. A fila é usada quando os elementos precisam ser processados na ordem em que chegam, como em sistemas de gerenciamento de tarefas, onde a primeira tarefa a ser chegada é a primeira a ser processada.

### Características:
- Na fila, os elementos são inseridos no final (final da fila) e removidos do início (início da fila).
- A fila é comumente usada em sistemas de processamento de dados em ordem, como impressoras, sistemas de mensagens e gerenciadores de tarefas.

### Operações principais:
- **Enfileirar (enqueue)**: Inserir um elemento no final da fila.
- **Desenfileirar (dequeue)**: Remover o elemento do início da fila.
- **Verificar o primeiro (peek)**: Acessar o primeiro elemento da fila sem removê-lo.
- **Verificar se está vazia (is_empty)**: Verificar se a fila está vazia.

---

Essas três estruturas são fundamentais para muitos tipos de algoritmos e são frequentemente usadas para resolver uma variedade de problemas computacionais, desde simples manipulações de dados até tarefas mais complexas de gerenciamento de memória e processamento de eventos.

