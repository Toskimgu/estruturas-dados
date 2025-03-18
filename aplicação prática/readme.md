Aplicação Prática: Gerenciador de Tarefas com Filas
Na aplicação prática de hoje, vamos resolver um problema comum em sistemas de gerenciamento de tarefas, utilizando a estrutura de dados fila.

Problema: Gerenciador de Tarefas
Imagine que você tem um sistema que precisa gerenciar um conjunto de tarefas. Cada tarefa deve ser processada na ordem em que foi recebida. Ou seja, a tarefa que foi adicionada primeiro deve ser a primeira a ser executada.


Esse tipo de comportamento é muito comum em sistemas de filas de espera, como:


Sistemas de atendimento ao cliente.
Processadores de impressão.
Gerenciamento de tarefas em sistemas operacionais.


Solução: Usando Fila (FIFO)
A estrutura de dados mais adequada para resolver esse problema é a fila (FIFO), pois ela garante que a primeira tarefa inserida será a primeira a ser processada (First In, First Out). Usaremos a operação de enfileirar para adicionar tarefas na fila e a operação de desenfileirar para processar e remover as tarefas da fila.


Como Funciona:
Enfileirar: Quando uma nova tarefa for criada, ela será adicionada ao final da fila.
Desenfileirar: O sistema processará a tarefa mais antiga (a primeira da fila), removendo-a da fila.
Acessar: Podemos acessar a próxima tarefa a ser processada, sem removê-la da fila.
Essa abordagem garante que as tarefas sejam tratadas na ordem em que chegam, respeitando a sequência.

