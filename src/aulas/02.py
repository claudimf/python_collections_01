idades = [39, 30, 27, 18, 15]
print(idades)

print(28 in idades)

print(15 in idades)

if 15 in idades:
    idades.remove(15)
    print(idades)

idades.insert(0, 20)
print(idades)

idades.append([27, 19])
print(idades)

for elemento in idades:
    print('Recebi o elemento', elemento)


idades = [39, 30, 27, 18, 15]
idades.extend([27, 19])
print(idades)

for idade in idades:
    print(idade + 1)

idades_no_ano_que_vem = []

for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)

print(idades_no_ano_que_vem)

idades_no_ano_que_vem = [(idade+1) for idade in idades]
print(idades_no_ano_que_vem)

idades_maior_que_21 = [(idade) for idade in idades if idade > 21]
print(idades_maior_que_21)


def proximo_ano(idade):
    return idade + 1

idades_no_ano_que_vem = [proximo_ano(idade) for idade in idades]
print(idades_no_ano_que_vem) 
