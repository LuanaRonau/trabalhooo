from datetime import date
from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, data_nasc: date):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nasc = data_nasc
        self.__atividade = False

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nasc(self):
        return self.__data_nasc

    @property
    def atividade(self):
        return self.__atividade

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @data_nasc.setter
    def data_nasc(self, data_nasc: date):
        self.__data_nasc = data_nasc

    @atividade.setter
    def atividade(self, atividade: bool):
        self.__atividade = atividade
