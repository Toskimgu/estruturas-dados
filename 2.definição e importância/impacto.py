# Código eficiente
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()  # Método otimizado de ordenação

print("Lista ordenada com estrutura eficiente:", numeros)

#-------------------------------------------------------------------------------------------------------------#

# Exemplo de código mostrando a diferença de desempenho entre um código ineficiente e um eficiente

# Código ineficiente - Ordenação usando abordagem de comparação dupla (O(n²))
def ordenar_ineficiente(numeros):
    for i in range(len(numeros)):
        for j in range(len(numeros)):
            if numeros[i] < numeros[j]:
                numeros[i], numeros[j] = numeros[j], numeros[i]
    return numeros

# Código eficiente - Ordenação utilizando o método sort() (O(n log n))
def ordenar_eficiente(numeros):
    numeros.sort()
    return numeros

# Lista de exemplo
numeros = [5, 2, 9, 1, 5, 6]

# Testando o código ineficiente
print("Usando código ineficiente:")
numeros_ineficiente = numeros.copy()
resultado_ineficiente = ordenar_ineficiente(numeros_ineficiente)
print("Resultado:", resultado_ineficiente)

# Testando o código eficiente
print("\nUsando código eficiente:")
numeros_eficiente = numeros.copy()
resultado_eficiente = ordenar_eficiente(numeros_eficiente)
print("Resultado:", resultado_eficiente)
