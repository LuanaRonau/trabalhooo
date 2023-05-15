from entidade.gerente import Gerente
from entidade.fun_comum import FunComum

class Filial:
    def __init__(self, cep: int, cidade: str, gerente: Gerente):
        self.__cep = cep
        self.__cidade = cidade
        self.__funcionarios = []
        self.__gerente = gerente

    @property
    def cep(self):
        return self.__cep

    @property
    def cidade(self):
        return self.__cidade

    @property
    def funcionarios(self):
        return self.__funcionarios

    @property
    def gerente(self):
        return self.__gerente

    @cep.setter
    def cep(self, cep):
        if isinstance(cep, str):
            self.__cep = cep

    @cidade.setter
    def cidade(self, cidade):
        if isinstance(cidade, str):
            self.__cidade = cidade

    def add_funcionario(self, funcionario: FunComum):
        self.__funcionarios.append(funcionario)

    def rem_funcionario(self, funcionario: FunComum):
        self.__funcionarios.append(funcionario)

    @gerente.setter
    def gerente(self, gerente: Gerente):
        self.__gerente = gerente
