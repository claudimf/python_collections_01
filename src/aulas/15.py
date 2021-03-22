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

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

print(conta_do_guilherme < conta_da_daniela)

print(conta_do_guilherme > conta_da_daniela)

for conta in sorted(contas):
    print(conta)


for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
    print(conta)
