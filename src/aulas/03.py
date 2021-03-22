def faz_processamento_de_visualizacao(lista):
    print(len(lista))

idades = [16, 21, 29, 56, 43]

faz_processamento_de_visualizacao(idades)
print(idades)


def faz_processamento_de_visualizacao(lista):
    print(len(lista))
    lista.append(13)

faz_processamento_de_visualizacao(idades)
print(idades)


def faz_processamento_de_visualizacao(lista=None):
    if lista is None:
        lista = list()
        print(len(lista))
        lista.append(13)


x = faz_processamento_de_visualizacao()
print(x)

x = faz_processamento_de_visualizacao()
print(x)
