from entidade.funcionario import Funcionario
from datetime import date

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, data_nasc: date):
        super().__init__(nome, cpf, data_nasc)
        self.__contratos = []

    @property
    def contratos(self):
        return self.__contratos

    @property
    def nome(self):
        return super().nome

    @property
    def cpf(self):
        return super().cpf

    @property
    def data_nasc(self):
        return super().data_nasc

    @property
    def atividade(self):
        return super().atividade

    @nome.setter
    def nome(self, nome):
        self._Funcionario__nome = nome

    @cpf.setter
    def cpf(self, cpf: str):
        self._Funcionario__cpf = cpf

    @data_nasc.setter
    def data_nasc(self, data_nasc: str):
        self._Funcionario__data_nasc = data_nasc

    @atividade.setter
    def atividade(self, atividade: bool):
        self._Funcionario__atividade = atividade

    def add_contrato(self, contrato):
        self.__contratos.append(contrato)

    def rem_contrato(self, contrato):
        self.__contratos.remove(contrato)