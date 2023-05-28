def verifica_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True
    
print(verifica_primo(5))   # Resultado: True
print(verifica_primo(10))  # Resultado: False
print(verifica_primo(17))  # Resultado: True
print(verifica_primo(25))  # Resultado: False