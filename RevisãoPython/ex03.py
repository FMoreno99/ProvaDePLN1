import random 

#Escolha um número entre 1 e 6
num_escolhido = int(input("Escolha um número entre 1 e 6: "))

#O programa vai sortear um número entre 1 e 6
num_sorteado = random.randint(1, 6)

#Vence se o número escolhido for igual ao número sorteado
ganhou = num_escolhido == num_sorteado

#Saidas
print(f"Você escolheu: {num_escolhido}")
print(f"Número sorteado: {num_sorteado}")
print(f"Você ganhou: {ganhou}")

#Condicional
if ganhou:
    print("Parabéns, você ganhou!")
else:
    print("Que pena, tente novamente!")