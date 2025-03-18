# fila.py
from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()

    def enfileirar(self, item):
        self.fila.append(item)  # Adiciona ao final da fila

    def desenfileirar(self):
        return self.fila.popleft()  # Remove o primeiro item

    def primeiro(self):
        return self.fila[0]  # Acessa o primeiro item

# Exemplo de uso
minha_fila = Fila()
minha_fila.enfileirar(10)
minha_fila.enfileirar(20)
print(minha_fila.desenfileirar())  # Saída: 10
print(minha_fila.primeiro())  # Saída: 20
