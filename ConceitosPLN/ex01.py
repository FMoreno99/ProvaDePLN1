import string
from string import punctuation
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")


def normalizar_texto(texto):
    mascara = str.maketrans("\n\r", "  ", punctuation)
    texto = texto.lower()
    texto = texto.translate(mascara)
    texto = texto.replace("  ", " ")
    return texto

def tokenizacao(texto):
    return word_tokenize(texto)

def gerar_vocabulario(tokens):
    vocabulario = []
    for token in tokens:
        if token not in vocabulario:
            vocabulario.append(token)
    return vocabulario

def analisar_riqueza(nome_musica, texto_bruto):
    texto_norm = normalizar_texto(texto_bruto)
    tokens = tokenizacao(texto_norm)
    vocab = gerar_vocabulario(tokens)
    
    total_tokens = len(tokens)
    tamanho_vocab = len(vocab)
    riqueza = tamanho_vocab / total_tokens if total_tokens > 0 else 0
    
    print(f"=== {nome_musica} ===")
    print(f"Total de Tokens: {total_tokens}")
    print(f"Tamanho do Vocabulário: {tamanho_vocab}")
    print(f"Riqueza Lexical: {riqueza:.4f} ({riqueza * 100:.2f}%)\n")


musica_djonga = """
Homem negro, inferno branco, tipo Tarantino
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
Te corto com meu sabre

Como se fosse a noite, cê vê tudo preto
Como fosse um blackout, cê vê tudo preto
São meus manos, minhas minas
Meus irmãos, minhas irmãs, yeah
O mundo é nosso, hã
Tipo a noite, cê vê tudo preto
Tipo um blackout, cê vê tudo preto
São cantos de esquinas, de reis e rainhas
Yeah, o mundo é nosso

Já disse, pretos no topo, e eu falava sério
Tipo BK, me veja como exemplo
Minha quebrada na merda, minha city fora do mapa, mano
Pros meus irmão eu sou exemplo, não nasci branco
Para ser franco, não nasci banco
Mesmo assim a Paty quer sentar
Sou elétrico, tenho em mim a resistência
Sou DV Afrotribo pondo fim na concorrência
Ganhar dinheiro tipo Cassino de Scorsese
Gastar dinheiro tipo Até Que a Sorte Nos Separe
Manos se drogam, pensam: Até que a morte nos ampare
E a bola de cristal do boy é a taça de Campari
E o morro chora, desespero e ainda tem barro lá
Prefeito diz: Senhor é meu pastor, mas nada te asfaltará
Tudo te faltará, se comprometerá
Pra consumir doses de alegria, e não pagará
É o Homem na Estrada de todo dia
E sabe a resposta, o que é clara e salgada
Os mais novo vive queimando largada
Não sabe ler nem escrever e sabe o nome da delegada
Sejamos Abraham Lincoln, independência
Com a pele de Barack Obama
Sejamos Tupac Shakur, Afeni Shakur
Achemos a cura pra nossa insegurança
Cada bala de fuzil é uma lágrima de Oxalá
Mas na rua né não, na mão dos cana né não
Na cintura era um celular e eles confundem com um oitão

Como se fosse a noite, cê vê tudo preto
Como fosse um blackout, cê vê tudo preto
São meus manos, minhas minas
Meus irmãos, minhas irmãs, yeah
O mundo é nosso, hã
Tipo a noite, cê vê tudo preto
Tipo um blackout, cê vê tudo preto
São cantos de esquinas, de reis e rainhas
Yeah, o mundo é nosso
"""

musica_bk = """
Esse é meu universo, onde eu me deito
Onde eu sonho, crio os monstros e os destruo
Esse é meu universo, onde eu me deito
Onde eu sonho, crio os monstros e os destruo

Olha pra mim! Olha pra Lapa!
Você sabe qual a cor da faixa?
Não parou no tempo e o tempo passa
E ainda tenho muito pra aprender
Pra aprender!
Olha pra mim! Olha pra Lapa!
Você sabe qual a cor da faixa?
Não parou no tempo e o tempo passa
E ainda tenho muito pra aprender
Pra aprender!
Olha pra

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
Seus amores, seus filhos, condutores e conduzidos, ok?

Eu nunca perco, é tudo troca
Eu sempre deixo, o que é meu volta
Eu nunca perco, é tudo troca
Eu sempre deixo, o que é meu volta

Olha pra mim! Olha pra Lapa!
Você sabe qual a cor da faixa?
Não parou no tempo e o tempo passa
E ainda tenho muito pra aprender
Pra aprender!
Olha pra mim! Olha pra Lapa!
Você sabe qual a cor da faixa?
Não parou no tempo e o tempo passa
E ainda tenho muito pra aprender
Pra aprender!
Olha pra

Não posso sair, isso é tipo um pacto
Minha missão, e por isso eu mato
Nasci pra isso, é meu destino
É meu caminho, o mundo tem me guiado
Não desista agora
Pense que isso é uma corrida onde não importa a volta
E não importa quem vai chegar em primeiro
E sim onde tu quer chegar, qual tua meta? Mostra!
Hey, tropa brindando, isso é fartura
Os bosta invejando, isso é loucura
Tá tudo aí na bandeja, uns querem ser, outros que ninguém seja
Não tive medo dos sacrifícios nem dos preços
Nem dos pesos, segui minha fome
Não me perdi nos elogios, fui avante

O dinheiro não é meu, esse tênis não é meu
Essa roupa não é minha, só tenho minha vida
Pode tirar de mim, ela nunca vai ser sua
Eu só tenho minha vida
O dinheiro não é meu, esse tênis não é meu
Essa joia não é minha, só tenho minha vida
Pode tirar de mim, ela nunca vai ser sua
Eu só tenho minha vida

Olha pra mim! (Olha pra Lapa!)
Você sabe qual a cor da faixa? (yeah, yeah)
Não parou no tempo e o tempo passa (yeah, yeah)
E ainda tenho muito pra aprender (pra aprender!)
Olha pra mim! (Olha pra Lapa!)
Você sabe qual a cor da faixa? (yeah, yeah)
Não parou no tempo e o tempo passa (yeah, yeah)
E ainda tenho muito pra aprender (pra aprender!)
Olha pra Lapa 
"""

musica_matue = """
Vet do 085, 085 (Fortal)
085, 085 (resgata o Brandão)
Vet do 085, 085
Quiseram me mudar, mas eu vim pra representar, meu lugar é no

085, 085 (é s—, é sal)
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
Tem umas barata que a gente vai ter que exterminar

Você é um vacilão, nóis vai te limar
Você é um vacilão, nóis vai te limar
Plé, plé, plé, plé (bola um beck)
Bola mil becks, bola um beck
Bola mil becks, depois bola um beck
Bola mais um, depois bola um beck (yeah-yeah-yeah)

Você é um vacilão, nóis vai te limar (yeah)
Você é um vacilão, nóis vai te limar
Plé, plé, bola um beck
Bola mil becks, depois bola um beck
Bola mil becks, depois bola um beck
Bola mais um beck, yeah-ahn-ahn

Não vai vacilar, para, para
Não vai vacilar (yeah)
Não, não, não, não, não
Não vai vacilar, maninho
Não vai vacilar, maninho
Não vai vacilar, não, ah

Único hash que eu conheço, eu fumo (yeah)
Morto não fala, tu virou defunto
Quis pagar de esperto e se saiu foi burro
Eu vi que o problema era esses mano imundo (yeah)
Ele se faz de gangsta e é playboy no fundo (tu é um boy)
A missão é uma: Dominar o mundo
Se tentar atravessar, nego, tu vai se frustrar
Não acompanha, que tu vai perder o rumo (yeah-ah)
O rumo, perder o rumo (yeah-yeah)
Tu vai perder o rumo (yeah-yeah)
Gang, gang, gang, gang

Os mano que tentou me atrapalhar foi pra último
Bolando uma bomba no Jaguar, mano, eu tô no jogo
Calma, não tem mais o que fazer, é o fundo do poço
Pra te exterminar só foi preciso eu acender outro (perfect)
Bola mais um beck (yeah)
Bola mais um pra nóis, que nóis vai fumar e fazer o rec (manda um)
Ela me mama na pia, não suja a calça que sou fashion (yeah)
Estampa de cruz na minha calça que eu sou fashion

Tô bebendo lean (yeah)
Puta e droga em mim (yeah)
Droga, arma em mim (yeah)
Grife e joia em mim (yeah)
Viver tranquilin (yeah)
Puta, droga em mim (yeah)
Droga, arma em mim (yeah)
Sonhos de vetin

Vetin, vetin (vetin, baby)
Vetin, vetin, sonhos de vetin (wow-wow)
Vetin, vetin (vetin, baby) (wow-wow)
Vetin, vetin, sonhos de vetin

Você é um vacilão, nóis vai te limar
Você é um vacilão, nóis vai te limar (sonhos de vetin)
Você é um vacilão, nóis vai te limar (você é um vacilão)
Você é um vacilão, nóis vai te limar (você é um vacilão)
Você é um vacilão, nóis vai te limar (vacilão, uou-uh, vacilão)
Você é um vacilão, nóis vai te limar (para de vacilar, ayy, vacilação)
Você é um vacilão, nóis vai te limar (você é um vacilão)
Você é um vacilão, nóis vai te limar (você é um vacilão)
"""

analisar_riqueza("O Mundo É Nosso - Djonga", musica_djonga)
analisar_riqueza("Universo - BK'", musica_bk)
analisar_riqueza("Isso é Sério - Matuê", musica_matue)