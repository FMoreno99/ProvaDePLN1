# Importa a biblioteca matplotlib.pyplot com o apelido padrão 'plt'
import matplotlib.pyplot as plt

# 1. Criação dos dados
# Eixo X: as categorias ou nomes dos documentos
documentos = ["Texto 1", "Texto 2", "Texto 3", "Texto 4", "Texto 5"]

# Eixo Y: os valores numéricos correspondentes a cada documento[cite: 61]
quantidade_palavras = [120, 180, 150, 210, 240]

# 2. Desenhando o gráfico de linhas
# plt.plot conecta os pontos informados utilizando linhas[cite: 57]
# O parâmetro marker='o' adiciona as bolinhas (marcadores) nos pontos exatos dos dados[cite: 64]
plt.plot(documentos, quantidade_palavras, marker='o', color='blue')

# 3. Adicionando os textos explicativos (Labels e Título)[cite: 59]
# title() adiciona o título principal do gráfico[cite: 59]
plt.title("Quantidade de palavras por documento")

# xlabel() adiciona o nome do eixo X (horizontal)[cite: 59]
plt.xlabel("Documentos")

# ylabel() adiciona o nome do eixo Y (vertical)[cite: 59]
plt.ylabel("Quantidade de palavras")

# 4. Mostrando o resultado
# Mostra o gráfico pronto na tela do computador[cite: 60]
plt.show()