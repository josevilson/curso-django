print('hello world')


class Agencia:
    def __init__(self, cnpj, endereco):
        self.cnpj = cnpj
        self.endereco = endereco

    def exibir_cnpj(self):
        return print(self)
