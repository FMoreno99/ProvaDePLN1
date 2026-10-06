#1 Maior posse de bola
posse_de_bola = 60
maior_posse = posse_de_bola >= 50  # True

#2 Zona de rebaixamento
pontuacao = 50
zona_de_rebaixamento = pontuacao < 45  # False

#3 Título mundial do Palmeiras
mundial_do_palmeiras = 0
tem_mundial = mundial_do_palmeiras > 0  # False

#4 Maior campeão paulista
corinthians = 31
maior_campeao = corinthians > 30  # True

#ex2

#1
titulo_posse = maior_posse and maior_campeao # True

#2
torcida_feliz = maior_campeao or zona_de_rebaixamento # True    

#3
abel_ferreira = tem_mundial and maior_posse # False 

#4
torcida_triste = zona_de_rebaixamento or tem_mundial # False

#5
sccp = maior_campeao or tem_mundial # True

#6
carrile = maior_campeao ^ maior_posse # False

#7
derby = maior_campeao ^ tem_mundial # True 

#8 
dinizismo = tem_mundial ^ maior_posse # True