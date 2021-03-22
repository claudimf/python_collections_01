class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Código {} e Saldo {}<<]".format(self.codigo, self.saldo)


conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])

deposita_para_todas(contas)
print(contas[0], contas[1])

guilherme = ('Guilherme', 37, 1981) # tupla
daniela = ('Daniela', 31, 1987)


def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

conta_do_gui = (15, 1000)
# conta_do_gui.deposita()
conta_do_gui = deposita(conta_do_gui)
print(conta_do_gui)


usuarios = [guilherme, daniela]
usuarios.append(('Paulo', 39, 1979))

contas = (guilherme, daniela)
