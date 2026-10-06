import numpy as np

# A matriz é criada com o formato especificado no exercício[cite: 45].
frequencias = np.array([
    [3, 0, 1, 2],
    [0, 2, 4, 1],
    [1, 1, 0, 5]
])

# 1. Qual o shape da matriz?
# O atributo .shape retorna uma tupla indicando (linhas, colunas)[cite: 11].
print("Shape da matriz:", frequencias.shape)

# 2. Quantos documentos existem?
# Como cada linha corresponde a um documento[cite: 45], acessamos a posição 0 do shape.
print("Quantidade de documentos:", frequencias.shape[0])

# 3. Quantas palavras existem no vocabulário?
# Como cada coluna corresponde a uma palavra[cite: 45], acessamos a posição 1 do shape.
print("Quantidade de palavras:", frequencias.shape[1])

# 4. Some a frequência total de cada palavra.
# Ao somar usando axis=0, o NumPy elimina o eixo das linhas e soma as colunas[cite: 41, 42].
soma_palavras = frequencias.sum(axis=0)
print("Soma por palavra:", soma_palavras)

# 5. Some a quantidade de palavras de cada documento.
# Ao somar usando axis=1, o NumPy elimina o eixo das colunas e soma as linhas[cite: 41, 42].
soma_documentos = frequencias.sum(axis=1)
print("Soma por documento:", soma_documentos)

# 6. Identifique quais valores são maiores que 2.
# O operador condicional cria uma máscara booleana (True/False) indicando as posições[cite: 31, 38].
maiores_que_dois = frequencias > 2
print("Valores maiores que 2:\n", maiores_que_dois)

# 7. Mostre apenas os elementos pares utilizando indexação e fatiamento.
# Usamos indexação com uma máscara onde o resto da divisão por 2 é zero (frequencias % 2 == 0)[cite: 38].
pares = frequencias[frequencias % 2 == 0]
print("Elementos pares:", pares)

# 8. Modifique este array para ter apenas uma dimensão.
# O método ravel() "achata" a matriz original, transformando-a em uma matriz unidimensional[cite: 25].
freq_1d = frequencias.ravel()

# 9. Mostre: média, mediana, desvio padrão.
# Utilizamos as funções de agregação diretas do NumPy[cite: 43].
media = freq_1d.mean()
mediana = np.median(freq_1d)
desvio = freq_1d.std()

print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio)