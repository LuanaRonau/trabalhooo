from entidade.filial import Filial
from entidade.funcionario import Funcionario
from datetime import date


class Transferencia:

    def __init__(self, id: int, funcionario: Funcionario,
                 filial_antiga: Filial,
                 filial_nova: Filial,
                 data: date):
        self.__id = id
        self.__funcionario = funcionario
        self.__filial_antiga = filial_antiga
        self.__filial_nova = filial_nova
        self.__data = data

    @property
    def id(self):
        return self.__id

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario):
            self.__funcionario = funcionario

    @property
    def filial_antiga(self):
        return self.__filial_antiga

    @filial_antiga.setter
    def filial_antiga(self, filial_antiga: Filial):
        if isinstance(filial_antiga, Filial):
            self.__filial_antiga = filial_antiga

    @property
    def filial_nova(self):
        return self.__filial_nova

    @filial_nova.setter
    def filial_nova(self, filial_nova: Filial):
        if isinstance(filial_nova, Filial):
            self.__filial_nova = filial_nova

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data


