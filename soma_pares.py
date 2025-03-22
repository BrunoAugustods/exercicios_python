def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

numeros = [2, 4, 10, 3, 9, 7, 15, 22, 6, 8]
resultado = soma_pares(numeros)
print(f"A soma dos pares é: {resultado}")
