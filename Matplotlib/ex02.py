import matplotlib.pyplot as plt

documentos = [1, 2, 3, 4, 5]
positivos = [120, 140, 170, 160, 190]
negativos = [150, 130, 180, 210, 200]

plt.plot(documentos, positivos, marker='o', label="Positivos")
plt.plot(documentos, negativos, marker='s', label="Negativos")

plt.title("Número médio de palavras por documento")
plt.xlabel("Documento")
plt.ylabel("Quantidade de palavras")
plt.legend()

plt.show()