import numpy as np

frequencias = np.array([
    [3, 0, 1, 2],
    [0, 2, 4, 1],
    [1, 1, 0, 5]
])

print("Shape da matriz:", frequencias.shape)
print("Quantidade de documentos:", frequencias.shape[0])
print("Quantidade de palavras:", frequencias.shape[1])

print("Soma por palavra:", frequencias.sum(axis=0))
print("Soma por documento:", frequencias.sum(axis=1))

print("Valores maiores que 2:\n", frequencias > 2)
print("Elementos pares:", frequencias[frequencias % 2 == 0])

freq_1d = frequencias.ravel()

print("Média:", freq_1d.mean())
print("Mediana:", np.median(freq_1d))
print("Desvio Padrão:", freq_1d.std())