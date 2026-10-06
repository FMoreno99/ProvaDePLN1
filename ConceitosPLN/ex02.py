import string
from string import punctuation
import nltk
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download("punkt")
nltk.download("punkt_tab")


def normalizar_texto(texto):
    """
    Substitui quebras de linha por espaço, remove pontuações
    e converte para letras minúsculas.
    """
    mascara_transformacao = str.maketrans("\n\r", "  ", punctuation)
    texto = texto.lower()
    texto = texto.translate(mascara_transformacao)
    texto = texto.replace("  ", " ")
    return texto

def tokenizacao(texto):
    """
    Tokeniza o texto utilizando o word_tokenize do NLTK.
    """
    return word_tokenize(texto)

def remover_stopwords(tokens, lista_stopwords):
    """
    Filtra os tokens utilizando o loop manual com 'if not in'.
    """
    tokens_limpos = []
    for token in tokens:
        if token not in lista_stopwords:
            tokens_limpos.append(token)
    return tokens_limpos


texto = """
A inteligência artificial está cada vez mais presente no nosso dia a dia.
A inteligência artificial pode ser utilizada para analisar textos,
reconhecer imagens e auxiliar na tomada de decisões.
A utilização da inteligência artificial em diferentes áreas está crescendo.
A tecnologia pode ajudar empresas a analisar grandes quantidades de dados
e pode auxiliar pessoas em diversas atividades.
"""

texto_normalizado = normalizar_texto(texto)
tokens = tokenizacao(texto_normalizado)


stopwords = [
    "a", "o", "os", "as", "de", "do", "da",
    "e", "em", "no", "na", "para", "ser"
]

tokens_filtrados = remover_stopwords(tokens, stopwords)

texto_nuvem1 = " ".join(tokens_filtrados)
wc1 = WordCloud(width=800, height=600)
img1 = wc1.generate(texto_nuvem1)

plt.figure(figsize=(10, 5))
plt.imshow(img1, interpolation="bilinear")
plt.axis("off")
plt.title("Nuvem 1 - Stopwords Iniciais")
plt.show()  

novas_stopwords = ["pode", "está", "cada"]
stopwords.extend(novas_stopwords)

tokens_finais = remover_stopwords(tokens, stopwords)

texto_nuvem2 = " ".join(tokens_finais)
wc2 = WordCloud(width=800, height=600)
img2 = wc2.generate(texto_nuvem2)

plt.figure(figsize=(10, 5))
plt.imshow(img2, interpolation="bilinear")
plt.axis("off")
plt.title("Nuvem 2 - Stopwords Atualizadas")
plt.show()