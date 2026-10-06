def buscar_linear(lista, valor_procurado):
    for i in range(len(lista)):
        if lista[i] == valor_procurado:
            return i  
    return -1 

numeros = [10, 25, 30, 45, 50]

posicao = buscar_linear(numeros, 30)
print(f"O valor 30 está no índice: {posicao}")  
posicao = buscar_linear(numeros, 99)
print(f"O valor 99 está no índice: {posicao}")  