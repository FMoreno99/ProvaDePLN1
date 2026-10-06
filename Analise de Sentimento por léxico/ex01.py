lexicon = dict()

nome_arquivo_lexico = "C:\\Users\\felip\\OneDrive\\Área de Trabalho\\lexico.txt"

with open(nome_arquivo_lexico, "r", encoding="utf-8") as arquivo_lexico:
    linha = " "
    while linha != "":
        linha = arquivo_lexico.readline()
        linha_split = linha.split(",")
        if len(linha_split) >= 3:
            chave = linha_split[0]
            valor = int(linha_split[2])
            lexicon[chave] = valor

print("Tamanho do Lexicon: ", len(lexicon))
print("-" * 30)

musica_djonga = """Homem negro, inferno branco, tipo Tarantino
Homem branco, inferno banto, tipo tá tirano
Os menor tá desesperado, tipo atirando
Eu querendo salvar o mundo, ela pergunta: Tá zuando?
É que as ruas me lembram Massacre da Serra Elétrica
Eles tentam roubar, é o massacre da cerca elétrica
E o rap preocupa com povo ou preocupa com a métrica
Mas os tentáculos do polvo é o que vai me afundar
E o olho que me julga precisa fazer regime
Ou algum de nós dois vai estar lá na cena do crime
E eu só querendo eu e minha mina na fila do cine
Vendo o filme da minha vitória
Sou da sua raça, mano, é a nossa vitória
Já foram farsa, vamo, contar nossa história
Quilombos, favelas, no futuro seremos reis, Charles
Seremos a negra mais linda desse baile, charme
A negra velha mais sábia, crianças a chave
Eles são cadeado, já foram corrente, sabe?
O lado negro da força, mato com meu sabre
Te corto com meu sabre"""

musica_bk = """Esse é meu universo, onde eu me deito
Onde eu sonho, crio os monstros e os destruo
Esse é meu universo, onde eu me deito
Onde eu sonho, crio os monstros e os destruo
Olha pra mim! Olha pra Lapa!
Você sabe qual a cor da faixa?
Não parou no tempo e o tempo passa
E ainda tenho muito pra aprender
Pra aprender!
Universo não vê bem, não vê mal, ele vê vontades
Que a minha vontade seja maior do que a dos meus inimigos
Universo não vê bem, não vê mal, ele vê verdades
Por que tu acha que eu não minto?
Até quando eu falo merda, isso é uma parte de quem sou
Não vou me fingir de bonzinho e depois te roubar, não sou pastor
Pode me achar de outro plano, mas o meu plano é o mesmo de todo mano
Carro do ano, bundas balançando, ninguém da casa chorando
Esse é o mundo real, onde reis sentem medo
Deuses não aguentam o peso, vontade se perde em desejo
Mas eu sei como o universo funciona, seus motores, seus fios
Seus amores, seus filhos, condutores e conduzidos, ok?"""

musica_matue = """Vet do 085, 085 (Fortal)
085, 085 (resgata o Brandão)
Vet do 085, 085
Quiseram me mudar, mas eu vim pra representar, meu lugar é no
Rolê de Benz, tô contando meus racks
Eu tô esperto, mas andando sem pressa
Não me testa que eu não quero conversa (ahn)
Ei, tu é quem? Meu irmão, isso é sério (isso é sério)
Eu tô com a gang, meu irmão, isso é sério (isso é sério)
Pingente brilhando, te deixa cego (uh)
Ela me viu e já chegou perto (ei)
Gravei meu nome nessas streets (hey, Tuê)
Fala françuê pra mim, me diz: Oui
Já que ela quer foder, então vai fluir
Nóis vamo firme e forte até o fim
Tava confuso na onda, perdido na onda (sem destino)
Procurando um novo caminho (sem rumo, sem volta)
Já que ela quer foder na onda (yeah)
Joga a bunda em cima de mim (yeah)
Minha mente corre de noite, é difícil desligar
Eu tô no corre, eu tô na posse da grana (cash)
Eu tô num Porsche em Fortal City na savana
Nessas ruas sujas, 12 mata, rato fala
A traição e a lealdade andam lado a lado
Toma cuidado com quem tu fala da tua vida
Tem umas barata que a gente vai ter que exterminar"""

print("Música: O Mundo É Nosso - Djonga")
corpus = musica_djonga.lower().replace("\n", " ").replace(",", "").replace(":", "").replace("?", "").replace("!", "").replace("  ", " ")
tokens = corpus.split(" ")

soma = 0
for token in tokens:
    if token != "":
        valor = lexicon.get(token, 0)
        soma += valor

print("O texto é: ", "POSITIVO" if soma > 0 else "NEGATIVO" if soma < 0 else "INDIFERENTE")
print("-" * 30)

print("Música: Universo - BK")
corpus = musica_bk.lower().replace("\n", " ").replace(",", "").replace(":", "").replace("?", "").replace("!", "").replace("  ", " ")
tokens = corpus.split(" ")

soma = 0
for token in tokens:
    if token != "":
        valor = lexicon.get(token, 0)
        soma += valor

print("O texto é: ", "POSITIVO" if soma > 0 else "NEGATIVO" if soma < 0 else "INDIFERENTE")
print("-" * 30)

print("Música: Isso é Sério - Matuê")
corpus = musica_matue.lower().replace("\n", " ").replace(",", "").replace(":", "").replace("?", "").replace("!", "").replace("(", "").replace(")", "").replace("  ", " ")
tokens = corpus.split(" ")

soma = 0
for token in tokens:
    if token != "":
        valor = lexicon.get(token, 0)
        soma += valor

print("O texto é: ", "POSITIVO" if soma > 0 else "NEGATIVO" if soma < 0 else "INDIFERENTE")