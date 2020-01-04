
#Script que vai dar erro
class Pessoa(object):
    def __init__(self, nome):
        self.__nome = nome

    def pega_nome(self):
        return self.__nome

ele = Pessoa('Pedro')
ele.pega_nome()
ele.__nome

#Script que vai dar certo
class Pessoa(object):
    def __init__(self, nome):
        self.__nome = nome

    def pega_nome(self):
        return self.__nome

ele = Pessoa('Pedro')
ele.pega_nome()
print(dir(ele))
ele._Pessoa__nome

#Exemplo herança
class Pessoa(object):
    def __init__(self, nome):
        self.__nome = nome

class Filha(Pessoa):
    def pega_nome(self):
        return self.__nome

ela = Filha('Pedro')
ela.pega_nome()

