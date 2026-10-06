# Importa a biblioteca NumPy com o apelido padrão 'np'[cite: 10]
import numpy as np

# Cria um array numérico contendo de 1 até 12[cite: 14]
# A função np.arange(inicio, fim) para sempre um número antes do "fim", por isso usamos 13[cite: 14]
# Isso representa o vocabulário de palavras convertidas em números para o algoritmo de PLN entender
vocabulario = np.arange(1, 13)

# O método .reshape() transforma o array de uma linha só (1D) em uma matriz (2D)[cite: 25]
# Aqui, dividimos os 12 elementos em 3 linhas e 4 colunas (3x4)[cite: 29]
matriz = vocabulario.reshape(3, 4)

# O atributo .T realiza a transposição da matriz (troca o que é linha por coluna e vice-versa)[cite: 27]
# Nossa matriz que era 3x4 vai virar uma matriz 4x3[cite: 27]
matriz_transposta = matriz.T

# Imprimimos os resultados para visualização no terminal
print("--- Array Original (Vocabulário de 1 a 12) ---")
print(vocabulario)

print("\n--- Matriz Redimensionada (3 linhas x 4 colunas) ---")
print(matriz)

print("\n--- Matriz Transposta (4 linhas x 3 colunas) ---")
print(matriz_transposta)