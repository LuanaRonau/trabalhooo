from telas.tela_mud_cargo import TelaMudCargo
from entidade.mud_cargo import MudancaCargo


class ControladorMudCargo:
    def __init__(self, control_sistema):
        self.__tela_mud = TelaMudCargo()
        self.__mudancas = []
        self.__control_sistema = control_sistema

    def incluir_mudanca(self):
        dados_mud_cargo = self.__tela_mud.pega_dados_mud_cargo()
        id = dados_mud_cargo["id"]
        data = dados_mud_cargo["data"]
        contrato = self.__control_sistema.controlador_contrato.pega_contrato_por_cpf(dados_mud_cargo["cpf"])
        func = contrato.empregado
        if dados_mud_cargo["promocao"] == "N":
            cargo_novo = self.__control_sistema.controlador_cargo.seleciona_cargo()
            contrato.add_mud_cargo(id, cargo_novo, func, data)
        else:
            contrato_f = self.__control_sistema.controlador_contrato.pega_contrato_por_cpf(contrato.empregador.cpf)
            self.__control_sistema.controlador_fun_comum_esp.excluir_cadastro(contrato.empregado)
            novo_gerente = {'nome': func.nome, 'CPF': func.cpf, 'data_nasc': func.data_nasc}
            self.__control_sistema.controlador_gerente.add_gerente(novo_gerente)
            self.__control_sistema.controlador_contrato.adiciona_fim_ao_contrato(contrato_f ,data)

    def alterar_mudanca(self):
        mudanca = self.seleciona_mud()
        novos_dados_mud_cargo = self.__tela_mud.pega_dados_mud_cargo(mudanca.id)
        contrato = self.__control_sistema.controlador_contrato.pega_contrato_por_cpf(mudanca.funcionario.cpf)
        mudanca.data = novos_dados_mud_cargo["data"]
        if novos_dados_mud_cargo["promocao"] == "N":
            self.__control_sistema.control_cargo.seleciona_cargo()
        else:
            mudanca.cargo_novo = self.__control_sistema.controlador_cargo.cargos[0]
            cpf_outro_gerente = contrato.filial.gerente.cpf
            contrato_outro_gerente = self.__control_sistema.controlador_contrato.pega_contrato_por_cpf(cpf_outro_gerente)
            self.__control_sistema.controlador_contrato.adiciona_fim_ao_contrato(contrato, novos_dados_mud_cargo["data"])

    def excluir_mudanca(self):
        mudanca = self.seleciona_mud()
        self.__mudancas.remove(mudanca)
        contrato = self.__control_sistema.controlador_contrato.pega_contrato_por_cpf(mudanca.funcionario.cpf)
        contrato.rem_mud_cargo(mudanca)

    def listar_mudancas(self):
        if len(self.__mudancas) == 0:
            self.__tela_mud.mostra_mensagem("Nenhuma mudança de cargo foi realizada.")
        else:
            for mud in self.__mudancas:
                self.__tela_mud.mostra_mud_cargo({"data": mud.data, "cargo_antigo": mud.cargo.titulo, "cargo_novo":
                                                  mud.cargo.titulo, "funcionario": mud.funcionario.nome, "id": mud.id})

    def listar_mudanca(self, mudanca):
        self.__tela_mud.mostra_mud_cargo({"data": mudanca.data, "cargo_antigo": mudanca.cargo.titulo, "id": mudanca.id,
                                          "cargo_novo": mudanca.cargo.titulo, "funcionario": mudanca.funcionario.nome})

    def seleciona_mud(self):
        self.listar_mudancas()
        id = self.__tela_mud.le_id("mudança de cargo")
        return self.pega_mud_por_id(id)

    def pega_mud_por_id(self, id):
        for mud in self.__mudancas:
            if mud.id == id:
                return mud

    def retornar(self):
        self.__control_sistema.inicializa_sistema()

    def abre_tela(self):
        lista_opcoes = {1}