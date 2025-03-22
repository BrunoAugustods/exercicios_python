def contagem_frequencia(lista):
    frequencia = {}
    for palavra in lista:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

palavras = ['Abilio', 'Abilio', 'Bernardo', 'Celso', 'Bernardo']
resultado = contagem_frequencia(palavras)
print(f"A contagem de frequências é: {resultado}")
