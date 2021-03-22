from operator import attrgetter


class ContaSalario():
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Código {} e Saldo {}<<]".format(self._codigo, self._saldo)

    def __eq__(self, outro):
        return self._codigo == outro._codigo and self._saldo == outro._saldo

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]


def extrai_saldo(conta):
    return conta._saldo


for conta in sorted(contas, key=extrai_saldo):
    print(conta)

for conta in sorted(contas, key=extrai_saldo, reverse=False):
    print(conta)


# utilizando o attrgetter

for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)

for conta in sorted(contas, key=attrgetter('_saldo'), reverse=False):
    print(conta)
