numeros = []
for numero in range(1000, 2001):
    if numero % 11 == 5:
        numeros.append(numero)

print(numeros)