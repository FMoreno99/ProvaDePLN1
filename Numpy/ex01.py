import numpy as np

vocabulario = np.arange(1, 13)

matriz = vocabulario.reshape(3, 4)

matriz_transposta = matriz.T

print(vocabulario)
print("-" * 20)
print(matriz)
print("-" * 20)
print(matriz_transposta)

