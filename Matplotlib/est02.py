import matplotlib.pyplot as plt

# 1. Criação dos dados extraídos da tabela[cite: 62]
documentos = [1, 2, 3, 4, 5]
positivos = [120, 140, 170, 160, 190]
negativos = [150, 130, 180, 210, 200]

# 2. Desenhando a primeira linha (Série Positivos)
# O parâmetro 'label' é essencial aqui, pois é ele que vai dar o nome para a legenda depois[cite: 63]
plt.plot(documentos, positivos, marker='o', color='green', label="Positivos")

# 3. Desenhando a segunda linha (Série Negativos) na mesma figura[cite: 63]
# Chamamos plt.plot() novamente para a segunda série[cite: 63]
plt.plot(documentos, negativos, marker='s', color='red', label="Negativos")

# 4. Adicionando textos explicativos (Labels e Título)[cite: 62]
plt.title("Número médio de palavras por documento")
plt.xlabel("Documento")
plt.ylabel("Quantidade de palavras")

# 5. Ativando a legenda
# A função legend() lê os 'labels' que definimos nos plt.plot() e cria a caixinha identificadora[cite: 63]
plt.legend()

# 6. Exibindo o gráfico
plt.show()