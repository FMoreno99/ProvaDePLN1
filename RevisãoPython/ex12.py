import os

tabela_substituicao = {
    'A': '4', 'a': '4',
    'B': '8', 'b': '8',
    'E': '3', 'e': '3',
    'G': '6', 'g': '6',
    'l': '1', 'L': '1',
    'q': '9', 'Q': '9',
    'S': '5', 's': '5',
    'T': '7', 't': '7',
    'Z': '2', 'z': '2'
}

nome_origem = input("Digite o nome/caminho do arquivo de origem: ")

with open(nome_origem, "r", encoding="utf-8") as arquivo_origem:
    conteudo_original = arquivo_origem.read()

texto_transformado = ""
for caractere in conteudo_original:
    if caractere in tabela_substituicao:
        texto_transformado += tabela_substituicao[caractere]
    else:
        texto_transformado += caractere

caminho_destino = "c:/temp/destino.txt"
os.makedirs("c:/temp", exist_ok=True)

with open(caminho_destino, "w", encoding="utf-8") as arquivo_destino:
    arquivo_destino.write(texto_transformado)

print("\n" + "=" * 40)
print("TEXTO TRANSFORMADO")
print(texto_transformado)
print("=" * 40)
print(f"\nArquivo salvo com sucesso em: {caminho_destino}")