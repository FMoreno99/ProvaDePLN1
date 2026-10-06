# Importa a biblioteca do matplotlib para desenhar os gráficos[cite: 49]
import matplotlib.pyplot as plt

# 1. Criação dos dados da curva (a linha de 3 pontos)
# Utiliza a mesma lógica do slide 60, gerando valores de X com saltos de 10[cite: 60]
x = range(-100, 110, 10)
y = []

# O laço for calcula a parábola invertida (y = -x²) que forma o arco central[cite: 60, 71]
for i in x:
    y.append(-i**2)

# 2. Desenhando a curva
# Conecta os pontos gerados formando a parábola azul[cite: 57, 71]
plt.plot(x, y)

# 3. Desenhando o Perímetro da Quadra
# axhline cria linhas horizontais e axvline cria linhas verticais[cite: 60]
# O atributo linewidth deixa a linha mais grossa para simular a borda da quadra[cite: 54, 71]
plt.axhline(0, linewidth=6)       # Linha superior[cite: 71]
plt.axhline(-2000, linewidth=6)   # Linha inferior[cite: 71]
plt.axvline(-75, linewidth=6)     # Linha lateral esquerda[cite: 71]
plt.axvline(75, linewidth=6)      # Linha lateral direita[cite: 71]

# 4. Adicionando nomes aos eixos[cite: 59, 71]
plt.xlabel("x")
plt.ylabel("y")

# 5. Definindo os limites visuais do gráfico
# xlim e ylim "cortam" o gráfico nos pontos exatos para formar o retângulo da quadra[cite: 64, 71]
plt.xlim(-76, 76)
plt.ylim(-2000, 0)

# Exibe o gráfico na tela[cite: 57]
plt.show()