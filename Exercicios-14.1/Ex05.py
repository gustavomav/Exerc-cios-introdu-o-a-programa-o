def encontra_palavras(lista_palavras, letra):
    palavras_iniciais = []
    for palavra in lista_palavras:
        if palavra.startswith(letra):
            palavras_iniciais.append(palavra)
    return palavras_iniciais

lista_palavras = ["casa", "gato", "carro", "lua", "computador", "limão"]
letra = "c"

palavras_iniciais = encontra_palavras(lista_palavras, letra)
print(palavras_iniciais)