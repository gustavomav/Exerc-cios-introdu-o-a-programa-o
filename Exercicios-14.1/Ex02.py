def calculo_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial
    
print(calculo_fatorial(5))  # Resultado: 120
print(calculo_fatorial(0))  # Resultado: 1
print(calculo_fatorial(1))  # Resultado: 1