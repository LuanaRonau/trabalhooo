from exception.jaEAFilialAtualException import JaEAFilialAtualException
from exception.jaEOCargoAtualException import JaEOCargoAtualException
from datetime import date
from entidade.funcionario import Funcionario
from entidade.gerente import Gerente
from entidade.filial import Filial
from entidade.mud_cargo import MudancaCargo
from entidade.transferencia import Transferencia
from entidade.cargo import Cargo

class Contrato:
    def __init__(self, id: int, data_inicio: date, cargo: Cargo, empregado: Funcionario, filial: Filial, empregador: Gerente):
        self.__id = id
        self.__data_inicio = data_inicio
        self.__data_final = None
        self.__cargo = cargo
        self.__empregado = empregado
        self.__filial = filial        
        self.__empregador = empregador
        self.__mud_cargos = []
        self.__transferencias = []

    @property
    def id(self):
        return self.__id

    @property
    def data_inicio(self):
        return self.__data_inicio

    @property
    def data_final(self):
        return self.__data_final

    @property
    def cargo(self):
        return self.__cargo

    @property
    def empregado(self):
        return self.__empregado

    @property
    def filial(self):
        return self.__filial

    @property
    def empregador(self):
        return self.__empregador

    @property
    def mud_cargos(self):
        return self.__mud_cargos
    
    @property
    def transferencias(self):
        return self.__transferencias
    
    @data_inicio.setter
    def data_inicio(self, data_inicio: date):
        self.__data_inicio = data_inicio

    @data_final.setter
    def data_final(self, data_final: date):
        if (data_final == None):
            if (not isinstance(self.__empregado, Gerente)):
                self.__filial.rem_funcionario(self.__empregado)
        self.__data_final = data_final

    @cargo.setter
    def cargo(self, cargo: Cargo):
        self.__cargo = cargo

    @empregado.setter
    def empregado(self, empregado: Funcionario):
        self.__empregado = empregado
        if (isinstance(empregado, Gerente)):
            self.__filial.gerente = empregado
        else:
            self.__filial.add_funcionario(empregado)

    @filial.setter
    def filial(self, filial: Filial):
        if (isinstance(self.__empregado, Gerente)):
            self.__filial = filial
            self.__filial.gerente = self.__empregador
        else:
            self.__filial.rem_funcionario(self.__empregado)
            self.__filial = filial
            self.__filial.add_funcionario(self.__empregado)

    @empregador.setter
    def empregador(self, empregador):
        self.__empregador = empregador
        self.__filial.gerente = empregador

    def add_transferencia(self, id: int, filial_nova: Filial, funcionario: Funcionario, data: date):
        if (filial_nova == self.__filial):
            raise JaEAFilialAtualException(filial_nova)
        self.__transferencias.append(Transferencia(id, funcionario, self.__filial, filial_nova, data))
        self.__filial = filial_nova

    def add_mud_cargo(self, id: int, cargo_novo: Cargo, funcionario: Funcionario, data: date):
        if (cargo_novo == self.__cargo):
            raise JaEOCargoAtualException(cargo_novo)
        self.__mud_cargos.append(MudancaCargo(id, self.__cargo, cargo_novo, funcionario, data))
        self.__cargo = cargo_novo
        
        if (cargo_novo.titulo == "Gerente"):
            self.__empregado = funcionario
            self.__empregador = "Empresa"

    def rem_transferencia(self, transferencia: Transferencia):
        self.__transferencias.remove(transferencia)
        self.__filial = transferencia.filial_antiga

    def rem_mud_cargo(self, mud_cargo: MudancaCargo):
        self.__mud_cargos.remove(mud_cargo)
        self.__cargo = mud_cargo.cargo_antigo
