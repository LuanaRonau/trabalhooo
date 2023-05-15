from telas.tela_contrato import TelaContrato
from entidade.contrato import Contrato

class ControladorContrato:

    def __init__(self, control_sistema):
        self.__contratos = []
        self.__tela_contrato = TelaContrato()
        self.__control_sistema = control_sistema

    def incluir_contrato(self, dados_contrato):
        if dados_contrato == None: # quando vindo do menu do contrato
            dados_contrato = self.__tela_contrato.pega_dados_contrato()
            id = dados_contrato["id"]
            data_inicio = dados_contrato["data_inicio"]
            cargo = self.__control_sistema.controlador_cargo.seleciona_cargo()
            empregado = self.__control_sistema.control_fun_comum.busca_func_por_cpf(dados_contrato["cpf"])
            filial = self.__control_sistema.busca_por_cep(dados_contrato["cep"])
            empregador = filial.gerente

        else:
            id = dados_contrato["id"]
            data_inicio = dados_contrato["data_inicio"]
            cargo = dados_contrato["cargo"]
            empregado = dados_contrato["empregado"]
            filial = dados_contrato["filial"]
            empregador = dados_contrato["empregador"]

        empregado.atividade = True

        novo_contrato = Contrato(id, data_inicio, cargo, empregado, filial, empregador)
        for contrato in self.__contratos:
            if (novo_contrato.data_inicio < contrato.data_inicio):
                self.__contratos.append(novo_contrato)
                break
        empregador.add_contrato(novo_contrato)

    def alterar_contrato(self):
        self.listar_contratos()
        id_contrato = self.__tela_contrato.le_id("contrato")
        contrato = self.pega_contrato_por_id(id_contrato)

        novos_dados_contrato = self.__tela_contrato.pega_dados_contrato(id_contrato)
        contrato.data_inicio = novos_dados_contrato["data_inicio"]
        contrato.empregado = self.__control_sistema.pega_func_por_cpf(novos_dados_contrato["cpf"])
        if (contrato.filial != novos_dados_contrato["filial"]):
            print("Filial não alterada, para alterá-la realize uma transferência.")
        self.listar_contrato(contrato)

    def pega_contrato_por_id(self, id: int):
        for contrato in self.__contratos:
            if (contrato.id == id):
                return contrato

    def listar_contratos(self):
        if (len(self.__contratos) == 0):
            self.__tela_contrato.mostra_mensagem("\nA empresa ainda não realizou nenhum contrato.")
        else:
            for contrato in self.__contratos:
                self.__tela_contrato.mostra_contrato({"empregador": contrato.empregador.nome, "id": contrato.id,
                                                      "empregado": contrato.empregado.nome, "cargo": contrato.cargo.titulo,
                                                      "filial": contrato.filial.cidade, "data": contrato.data_inicio})

    def relatorio_contrato_por_data(self):
        mes = 0
        for contrato in self.__contratos:
            if (contrato.data_inicio.month != mes):
                mes = contrato.data_inicio.month
                self.__tela_contrato.mostra_mensagem("\n" + contrato.data.strftime("%m/%Y"))
            self.listar_contrato(contrato)

    def listar_contrato(self, contrato):
        self.__tela_contrato.mostra_contrato({"empregador": contrato.empregador.nome, "id": contrato.id, "empregado":
                                              contrato.empregado.nome, "cargo": contrato.cargo.titulo,
                                              "filial": contrato.filial.cidade})

    def excluir_contrato(self):
        self.listar_contratos()
        id_contrato = self.__tela_contrato.le_id("contrato")
        contrato = self.pega_contrato_por_id(id_contrato)

        self.__contratos.remove(contrato)
        self.listar_contratos()
        self.__tela_contrato.exclui_id(id_contrato)

    def finalizar_contrato(self):
        self.listar_contratos()
        id_contrato = self.__tela_contrato.le_id("contrato")
        contrato = self.pega_contrato_por_id(id_contrato)
        data_encerramento = self.__tela_contrato.le_data("\nDigite a data de encerramento do contrato: ")
        contrato.data_final = data_encerramento
        contrato.empregado.atividade = False
        if (contrato.empregado.cargo.titulo == "Gerente"):
            self.__tela_contrato.mostra_mensagem("Segundo a política da empresa as filiais não podem ficar sem gerência"
                                                 ", por causa disso agora você será direcionado à tela de mudança de "
                                                 "cargo para promover um dos funcionários a gerente.")
            novo_gerente = self.__control_sistema.controlador_mud_cargo.incluir_mud_cargo()
            contrato.gerente = novo_gerente

    def adiciona_fim_ao_contrato(self, contrato, data):
        contrato.data_final = data
        contrato.empregado.atividade = False

    def pega_contrato_por_cpf_auto(self, cpf):
        for contrato in self.__contratos:
            if contrato.empregado.cpf == cpf:
                return contrato

    def historico_func(self):
        pass

    def retornar(self):
        self.__control_sistema.inicializa_sistema()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_contrato, 2: self.alterar_contrato, 3: self.excluir_contrato,
                        4: self.listar_contratos, 5: self.relatorio_contrato_por_data, 6: self.historico_func,
                        7: self.finalizar_contrato, 8: self.retornar()}

        continua = True
        while continua:
            lista_opcoes[self.__tela_contrato.mostra_opcoes()]()

