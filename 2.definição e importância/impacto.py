### Exemplo de Impacto no Desempenho

#### Código sem estrutura de dados adequada:

numeros = [5, 2, 9, 1, 5, 6]
for i in range(len(numeros)):
    for j in range(len(numeros)):
        if numeros[i] < numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

#### Código otimizado com estrutura de dados eficiente:

numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()  # Uso de algoritmo otimizado

print(numeros)  # Imprime a lista ordenada