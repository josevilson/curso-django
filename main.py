print('hello world')


class Agencia:
    def __init__(self, cnpj, endereco):
        self.cnpj = cnpj
        self.endereco = endereco
        self.numero = 52
        self.github = "teste de commit"

    def exibir_cnpj(self):
        return print(self)
