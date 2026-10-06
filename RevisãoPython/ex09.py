TOTAL_NUMEROS = 20

numeros = []

print(f"Digite {TOTAL_NUMEROS} números inteiros:")
for i in range(TOTAL_NUMEROS):
    valor = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(valor)

numeros_invertidos = list(reversed(numeros))
print("\n" + "=" * 35)
print(f"{'Numero':<10} {'Soma':<10} {'Media':<10}")
print("-" * 35)
soma_acumulada = 0

for i, num in enumerate(numeros_invertidos, start=1):
    soma_acumulada += num
    media = soma_acumulada / i
    print(f"{num:<10} {soma_acumulada:<10} {media:<10.2f}")