# lista.py
class Lista:
    def __init__(self):
        self.lista = []

    def inserir(self, item):
        self.lista.append(item)  # Adiciona item ao final da lista

    def remover(self, item):
        self.lista.remove(item)  # Remove o primeiro item encontrado

    def acessar(self, indice):
        return self.lista[indice]  # Acessa um item pelo índice

# Exemplo de uso
minha_lista = Lista()
minha_lista.inserir(10)
minha_lista.inserir(20)
minha_lista.remover(10)
print(minha_lista.acessar(0))  # Saída: 20
