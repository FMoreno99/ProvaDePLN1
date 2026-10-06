import spacy

nlp = spacy.load("pt_core_news_sm")

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

texto_manifesto = """A história de todas as sociedades que existiram até nossos dias tem sido a história das lutas de classes.
Homem livre e escravo, patrão e plebeu, senhor feudal e servo, mestre de corporação e oficial.
Em resumo, opressores e oprimidos, em constante oposição, têm vivido numa guerra ininterrupta.
Ora franca, ora disfarçada; uma guerra que terminou sempre por uma transformação revolucionária.
Ou pela destruição das duas classes em luta.
Nas primeiras épocas históricas, verificamos quase por toda parte uma divisão complexa da sociedade.
A sociedade organizava-se em classes distintas, uma escala graduada de condições sociais.
Na Roma antiga encontramos patrícios, cavaleiros, plebeus e escravos.
Na Idade Média, senhores feudais, vassalos, mestres de corporação, oficiais e servos.
Em quase todas essas classes encontramos gradações particulares.
A moderna sociedade burguesa, que brotou das ruínas da sociedade feudal, não aboliu os antagonismos.
Não aboliu os antagonismos de classes existentes.
Apenas substituiu as velhas classes por novas classes.
Substituiu velhas condições de opressão por novas condições de opressão.
Substituiu velhas formas de luta por novas formas de luta.
Entretanto, a nossa época, a época da burguesia, caracteriza-se por ter simplificado esses antagonismos.
A sociedade divide-se cada vez mais em dois vastos campos inimigos.
Divide-se em duas grandes classes diametralmente opostas: a burguesia e o proletariado.
Dos servos da Idade Média nasceram os vilões livres das primeiras cidades.
Desta população municipal saíram os primeiros elementos da burguesia.
A descoberta da América e a circunavegação da África abriram um novo campo à burguesia ascendente.
Os mercados das Índias Orientais e da China deram novo impulso ao comércio.
A colonização da América e o comércio colonial incrementaram as mercadorias e os meios de troca.
Imprimiram um impulso desconhecido até então ao comércio, à navegação e à indústria.
Desenvolveram rapidamente o elemento revolucionário da sociedade feudal em decomposição.
O antigo sistema feudal ou corporativo da indústria já não satisfazia as necessidades crescentes.
Essas necessidades aumentavam com a abertura de novos mercados.
A manufatura substituiu o sistema corporativo feudal de produção.
Os mestres de corporação foram postos de lado pela divisão do trabalho.
A divisão do trabalho entre as diversas corporações deu lugar à divisão na mesma oficina.
Os mercados continuavam a crescer e a procura continuava a aumentar.
A própria manufatura já não era mais suficiente para atender à demanda.
O vapor e as máquinas revolucionaram a produção industrial mundial.
A grande indústria moderna substituiu a manufatura tradicional.
O lugar da classe média industrial foi ocupado pelos milionários da indústria.
Grandes chefes de exércitos industriais, os modernos burgueses tomaram a frente.
A grande indústria criou o mercado mundial, preparado pela descoberta da América.
O mercado mundial deu um impulso imenso ao desenvolvimento do comércio.
Impulsionou a navegação e as comunicações por via férrea em todo o globo.
Esse desenvolvimento reagiu por sua vez sobre a extensão da indústria fabril.
À medida que a indústria, o comércio, a navegação e as ferrovias se desenvolviam.
Na mesma medida a burguesia crescia e multiplicava seus capitais.
Relegava a segundo plano as classes herdadas da Idade Média feudal.
Vemos, pois, como a própria burguesia moderna é o produto de um longo desenvolvimento.
É o fruto de uma série de transformações no modo de produção e de circulação.
Cada etapa desse desenvolvimento foi acompanhada de um progresso político correspondente.
Classe oprimida pelo despotismo dos senhores feudais na Idade Média.
Associação armada e auto-administrada na comuna medieval independente.
Aqui república urbana independente, ali terceiro estado tributário da monarquia.
Depois, no período manufatureiro, contrapeso à nobreza nas monarquias constitucionais.
Pedra angular das grandes monarquias em geral contra os nobres.
A burguesia conquistou finalmente a posse exclusiva do poder político moderno.
Conquistou o poder no moderno Estado representativo industrial.
O governo do Estado moderno não é mais do que um comitê para gerir os negócios comuns da burguesia.
A burguesia desempenhou na história um papel eminentemente revolucionário.
Onde quer que tenha conquistado o poder, destruiu as relações feudais e patriarcais.
Rasgou sem piedade os laços feudais que prendiam o homem aos seus superiores naturais.
Não deixou outro vínculo entre os seres humanos senão o frio interesse econômico.
Substituiu o laço humano pelo pagamento à vista e insensível.
Afogou o fervor do entusiasmo religioso na água gelada do cálculo egoísta.
Afogou a cavalheiresca exaltação e o sentimentalismo vulgar na busca do lucro.
Fez da dignidade pessoal um simples valor de troca nas relações humanas.
Substituiu as numerosas liberdades conquistadas por uma única liberdade: a de comércio.
Em lugar da exploração velada por ilusões religiosas e políticas estabeleceu uma exploração direta.
Uma exploração aberta, impudente, direta e descarada contra as massas.
A burguesia despojou de sua auréola todas as atividades até então honradas.
Atividades olhadas com respeito religioso foram transformadas em trabalho assalariado.
Transformou o médico, o jurista, o padre, o poeta e o homem de ciência em trabalhadores pagos.
A burguesia rasgou o véu de comovente sentimentalismo das relações de família.
Reduziu todas as relações familiares a meras relações monetárias e financeiras.
A burguesia revelou como a brutal manifestação de forças na Idade Média encontrou complemento.
Encontrou seu complemento na mais preguiçosa e completa indolência.
Foi a primeira a provar do que é capaz a atividade criadora dos seres humanos.
Realizou maravilhas que superam completamente as pirâmides do Egito e os aquedutos romanos.
Conduziu expedições que puseram na sombra todas as antigas migrações e cruzadas.
A burguesia não pode existir sem revolucionar continuamente os instrumentos de produção.
Não pode existir sem revolucionar as relações de produção e toda a sociedade.
A conservação inalterada do antigo modo de produção era a primeira condição de existência.
A revolução contínua da produção e a abalo constante de todas as condições sociais diferenciam a época.
Diferenciam a época burguesa de todas as épocas precedentes da história humana.
Todas as relações fixas e fossilizadas dissolvem-se com o cortejo de velhas ideias.
Todas as novas relações envelhecem antes de poderem se consolidar no tempo.
Tudo o que é sólido se desmancha no ar e evapora na atmosfera.
Tudo o que é sagrado é profanado pelos novos métodos do capital.
Os homens são finalmente obrigados a encarar suas reais condições de vida.
São forçados a encarar suas relações recíprocas sem qualquer ilusão mística.
A necessidade de novos mercados impulsiona a burguesia por todo o globo terrestre.
Precisa estabelecer-se em toda parte e explorar novas terras.
Precisa criar vínculos e mercados consumidores em todos os lugares.
Pela exploração do mercado mundial, a burguesia deu um caráter cosmopolita à produção.
Deu um caráter universal ao consumo em todos os países do mundo.
Para grande desespero dos reacionários, retirou a base nacional da indústria.
As velhas indústrias nacionais foram destruídas e continuam a ser destruídas diariamente.
São suplantadas por novas indústrias cuja introdução se torna questão de vida ou morte.
Indústrias que já não empregam matérias-primas nativas das próprias regiões.
Mas matérias-primas vindas das zonas mais remotas e distantes do mundo.
Indústrias cujos produtos se consomem em todos os quadrantes do globo terrestre.
Em lugar das antigas necessidades satisfeitas pela produção nacional nascem novas necessidades.
Necessidades cuja satisfação exige produtos das regiões e climas mais longínquos.
Em lugar da antiga auto-suficiência local e nacional surge o intercâmbio universal.
Desenvolve-se uma interdependência universal entre todas as nações do mundo.
E isso acontece tanto na produção material quanto na produção intelectual.
As criações intelectuais de uma nação tornam-se patrimônio comum de todas as demais.
A estreiteza e o isolamento nacionais tornam-se de dia para dia mais impossíveis de manter.
Das numerosas literaturas nacionais e locais forma-se uma literatura universal moderna.
Com o rápido aperfeiçoamento dos instrumentos de produção e comunicações mais fáceis.
A burguesia arrasta todas as nações, até as mais bárbaras, para a civilização.
Os preços baratos de suas mercadorias são a artilharia pesada que destrói muralhas.
Com essa artilharia derruba as muralhas da China e vence os mais obstinados preconceitos.
Obriga todas as nações a adotarem o modo de produção burguês sob pena de extinção.
Obriga-as a introduzir em seu seio a chamada civilização do capital.
Em suma, a burguesia moderna cria um mundo à sua própria imagem e semelhança."""

linhas = texto_manifesto.split("\n")

for linha_texto in linhas:
    if linha_texto != "":
        linha_limpa = linha_texto.lower().replace(",", "").replace(".", "").replace(";", "").replace(":", "").replace("?", "").replace("!", "").replace("  ", " ")
        
        tokens_spacy = nlp(linha_limpa)
        
        texto_lemma = ""
        for token in tokens_spacy:
            texto_lemma += token.lemma_ + " "
            
        tokens_limpos = texto_lemma.strip().split(" ")
        
        soma = 0
        for palavra in tokens_limpos:
            valor = lexicon.get(palavra, 0)
            soma += valor
            
        resultado = "POSITIVO" if soma > 0 else "NEGATIVO" if soma < 0 else "INDIFERENTE"
        
        print(linha_texto)
        print("Sentimento:", resultado)
        print("-" * 30)