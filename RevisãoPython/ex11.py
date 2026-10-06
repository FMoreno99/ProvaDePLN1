def busca_binaria(vetor, valor_procurado):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == valor_procurado:
            return meio  
        elif vetor[meio] < valor_procurado:
            inicio = meio + 1  
        else:
            fim = meio - 1  
    return -1  

vetor_ordenado = [10, 20, 30, 40, 50, 60, 70, 80, 90]

posicao = busca_binaria(vetor_ordenado, 40)
print(f"O número 40 está no índice: {posicao}") 

# Teste 2: Elemento ausente
posicao = busca_binaria(vetor_ordenado, 25)
print(f"O número 25 está no índice: {posicao}") 