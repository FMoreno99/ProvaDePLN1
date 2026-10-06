import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1. ENTRADA DE DADOS
texto = """
A inteligência artificial está cada vez mais presente no nosso dia a dia.
A inteligência artificial pode ser utilizada para analisar textos,
reconhecer imagens e auxiliar na tomada de decisões.
A utilização da inteligência artificial em diferentes áreas está crescendo.
A tecnologia pode ajudar empresas a analisar grandes quantidades de dados
e pode auxiliar pessoas em diversas atividades.
"""

# 2. LIMPEZA E TOKENIZAÇÃO
# Converte para minúsculas e remove pontuação
texto_limpo = texto.lower().translate(str.maketrans("", "", string.punctuation))

# Separa em lista de tokens[cite: 1]
tokens = texto_limpo.split()

# 3. PRIMEIRA REMOÇÃO DE STOPWORDS
stopwords = [
    "a", "o", "os", "as", "de", "do", "da",
    "e", "em", "no", "na", "para", "ser"
]

# Cria uma nova lista mantendo apenas as palavras que NÃO estão nas stopwords[cite: 1]
tokens_filtrados = [palavra for palavra em tokens if palavra not in stopwords]

# 4. PRIMEIRA NUVEM DE PALAVRAS
# A WordCloud pede um texto único, então juntamos os tokens filtrados com espaços
texto_para_nuvem = " ".join(tokens_filtrados)

nuvem1 = WordCloud(width=800, height=400, background_color="white").generate(texto_para_nuvem)
plt.figure(figsize=(10, 5))
plt.imshow(nuvem1, interpolation="bilinear")
plt.axis("off")
plt.title("Nuvem 1 - Stopwords Iniciais")
plt.show()

# 5. ATUALIZAÇÃO DE STOPWORDS
# Observando a Nuvem 1, verbos e advérbios comuns roubam a cena.
# Adicionamos "pode", "está" e "cada" à lista, pois não agregam sentido ao tema[cite: 1]
novas_stopwords = ["pode", "está", "cada", "mais", "nosso", "dia"]
stopwords.extend(novas_stopwords)

# 6. SEGUNDA REMOÇÃO DE STOPWORDS
# Filtramos novamente, agora com a lista de stopwords atualizada
tokens_finais = [palavra for palavra em tokens if palavra not in stopwords]

# 7. SEGUNDA NUVEM DE PALAVRAS
texto_final_nuvem = " ".join(tokens_finais)

nuvem2 = WordCloud(width=800, height=400, background_color="white").generate(texto_final_nuvem)
plt.figure(figsize=(10, 5))
plt.imshow(nuvem2, interpolation="bilinear")
plt.axis("off")
plt.title("Nuvem 2 - Stopwords Atualizadas")
plt.show()