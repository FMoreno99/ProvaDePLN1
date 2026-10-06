print("Triângulo")

for i in range(1, 6):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

#desafio
print("Desafio")

tamanho = int(input("Informe o tamanho do triângulo: "))

for i in range(1, tamanho + 1):
    print("*" * i)

for i in range(tamanho, 0, -1):
    print("*" * i)