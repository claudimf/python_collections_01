idades = [15, 87, 32, 65, 56, 32, 49, 37]

for idade in idades:
    print(idade)

range(len(idades))

for i in range(len(idades)):
    print(i)
    print(i, idades[i])


x = list(range(len(idades))) # Forcei a geração dos valores
print(x)

x = list(enumerate(idades))
print(x)

for valor in enumerate(idades):
    print(valor)


usuarios = [
    ('Guilherme', 37, 1981),
    ('Daniela', 31, 1987),
    ('Paulo', 39, 1979)
    ]

for nome, idade, nascimento in usuarios:
    print(nome)


for nome, _, _ in usuarios:
    print(nome)
