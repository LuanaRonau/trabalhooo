from entidade.funcionario import Funcionario
from datetime import date


class FunComum(Funcionario):
    def __init__(self, nome: str, cpf: str, data_nasc: date):
        super().__init__(nome, cpf, data_nasc)

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
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf: str):
        super().cpf = cpf

    @data_nasc.setter
    def data_nasc(self, data_nasc: str):
        super().data_nasc = data_nasc

    @atividade.setter
    def atividade(self, atividade: bool):
        super().atividade = atividade
