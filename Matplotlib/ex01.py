import matplotlib.pyplot as plt
import numpy as np
import spacy

nlp = spacy.load("pt_core_news_sm")

X = np.linspace(0, 10, 20)
temp = np.random.random(20)
Y = X * temp

fig, ax = plt.subplots(1, 2)
ax[0].plot(X, Y, color="green", linestyle="-.", linewidth=1, alpha=0.9, label="Teste")
ax[0].grid(True, color="red", linestyle="--", linewidth=1, alpha=0.1)
ax[0].set_xlabel("Ano Corrente")
ax[0].set_ylabel("Lucro")
ax[0].text(8, 0.5, "Pandemia")
ax[0].set_title("Lucro do ano atual")
ax[0].axhline(6.5)
ax[0].axvline(3)
ax[0].legend()

ax[1].barh(X, Y)
ax[1].set_xlabel("Meses")
ax[1].set_ylabel("Volume de Vendas")
ax[1].grid(True)

plt.tight_layout(pad=2)
plt.show()

pessoas = np.random.randint(12, 98, 100)
plt.hist(pessoas, bins=10, range=(30, 98), rwidth=0.8)
plt.show()

palavras = [100, 150, 200, 250, 300]
palavras_unicas = [65, 90, 110, 130, 145]
plt.scatter(palavras, palavras_unicas, s=30, color="blue")
plt.xlabel("Quantidade de palavras")
plt.ylabel("Palavras únicas")
plt.title("Tamanho do texto × Vocabulário")
plt.show()

activities = ['eat', 'sleep', 'work', 'studing', 'play']
slices = [3, 6, 6, 6, 3]
colors = ['yellow', 'blue', 'red', 'brown', 'green']

plt.pie(slices, labels=activities, colors=colors, startangle=0, 
        shadow=True, explode=(0, 0.2, 0, 0, 0), radius=1.2, autopct='%1.1f%%')
plt.legend(loc="upper right")
plt.show()