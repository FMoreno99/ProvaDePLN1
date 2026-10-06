TOTAL_ALUNOS = 10
TOTAL_NOTAS = 5

matriz_notas = []
todas_as_notas = []

print("DIGITE AS NOTAS")
for aluno in range(TOTAL_ALUNOS):
    print(f"Notas do Aluno {aluno + 1}:")
    notas_aluno = []
    
    for n in range(TOTAL_NOTAS):
        nota = float(input(f"Digite a nota {n + 1}: "))
        notas_aluno.append(nota)
        todas_as_notas.append(nota)
        
    matriz_notas.append(notas_aluno)

print("\n" + "=" * 35)
print("Notas dos Alunos:")
for i, notas in enumerate(matriz_notas, start=1):
    print(f"Aluno {i}: {notas}")

maior_nota = max(todas_as_notas)
menor_nota = min(todas_as_notas)

print(f"Maior nota registrada: {maior_nota:.2f}")
print(f"Menor nota registrada: {menor_nota:.2f}")
print("\n" + "=" * 35)
print("MÉDIA FINAL POR ALUNO")
for i, notas in enumerate(matriz_notas, start=1):
    media = sum(notas) / len(notas)
    print(f"Aluno {i} -> Média: {media:.2f}")