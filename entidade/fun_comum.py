from entidade.funcionario import Funcionario
from datetime import date


class FunComum(Funcionario):
    def __init__(self, nome: str, cpf: str, data_nasc: date):
        super().__init__(nome, cpf, data_nasc)

    @property
    def nome(self):
        return self._Funcionario__nome

    @property
    def cpf(self):
        return self._Funcionario__cpf

    @property
    def data_nasc(self):
        return self._Funcionario__data_nasc

    @property
    def atividade(self):
        return self._Funcionario__atividade

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
