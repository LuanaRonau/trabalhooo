from telas.tela_transf import TelaTransf
from entidade.transferencia import Transferencia
from exception.jaEAFilialAtualException import JaEAFilialAtualException
from exception.funcInativoException import FuncInativoException

class ControladorTransf:

    def __init__(self, control_filial):
        self.__tela_transf = TelaTransf()
        self.__control_filial = control_filial
        self.__transferencias =[]

    def incluir_transf(self, dados_transf=None):
        while True:
            try:
                if dados_transf == None:
                    dados_transf = self.__tela_transf.pega_dados_transf()
                data = dados_transf["data"]
                id = dados_transf["id"]
                filial_nova = self.__control_filial.pega_filial_por_cep(dados_transf["cep_filial_nova"])
                contrato = self.__control_filial.control_contrato.pega_contrato_por_cpf_auto(dados_transf["cpf"])
                filial_antiga = contrato.filial
                gerente_da_filial_nova = filial_nova.gerente

                if (contrato.empregado.cargo.titulo != "Gerente"):
                    funcionario = self.__control_filial.control_func.pega_func_por_cpf(dados_transf["cpf"])
                    funcionario.gerente = gerente_da_filial_nova
                else:
                    funcionario = self.__control_filial.control_gerente.pega_gerente_por_cpf(dados_transf["cpf"])

                if (funcionario.atividade == False):
                    raise FuncInativoException

                nova_transf = contrato.add_transf(id, filial_nova, funcionario, data)
                for transf in self.__transferencias:
                    if (nova_transf.data < transf.data):
                        self.__transferencias.append(nova_transf)
                self.listar_transf(nova_transf)

                if (contrato.empregado.cargo.titulo == "Gerente"):
                    op = self.__tela_transf.opcao_gerente()
                    cpf_outro_gerente = gerente_da_filial_nova.cpf
                    contrato = self.__control_filial.control_contrato.pega_contrato_por_cpf_auto(cpf_outro_gerente)

                    if (op == 1): # inverter gerentes
                        id = self.__tela_transf.gera_id()
                        nova_transf = contrato.add_transf(id, filial_antiga, gerente_da_filial_nova, data)
                        self.__transferencias.append(nova_transf)
                        self.listar_transf(nova_transf)

                    else: # demitir gerente anterior e promover func
                        self.__control_filial.control_contrato.finalizar_contrato(contrato)
                        self.__control_filial.control_mud_cargo.incluir_mud_cargo()
                return
            except FuncInativoException:
                self.__tela_transf.mostra_mensagem("Impossível realizar transferência pois o funcionário não está ativo"
                                                   " na empresa.")
            except JaEAFilialAtualException:
                print(JaEAFilialAtualException)

    def alterar_transf(self):
        self.listar_transfs()
        id_transf = self.__tela_transf.le_id("transferência")
        transf = self.pega_transf_por_id(id_transf)

        atributo = self.__tela_transf.escolha_alteracao()

        if (atributo == 1):
            cpf = self.__tela_transf.le_cpf_valido()
            contrato_novo = self.__control_filial.control_contrato.pega_contrato_por_cpf_auto(cpf)
            func_novo = contrato_novo.empregado
            func_anterior = transf.funcionario
            contrato_anterior = self.__control_filial.control_contrato.pega_contrato_por_cpf_auto(func_anterior.cpf)

            if (func_novo.cargo.titulo != "Gerente") and (func_anterior.cargo.titulo != "Gerente"):
                transf.funcionario = func_novo
                contrato_anterior.rem_transferencia(transf)
                contrato_novo.add_transferencia(id_transf, transf.filial_nova, func_novo, transf.data)
        elif (atributo == 2):
            cep = self.__tela_transf.verifica_cep_valido("Digite o CEP da filial: [XXXXX-XXX] ")
            filial = self.__control_filial.pega_filial_por_cep(cep)
            transf.filial_nova = filial
            contrato = self.__control_filial.pega_contrato_por_cpf(transf.funcionario.cpf)
            contrato.filial = filial
        else:
            transf.data = self.__tela_transf.verifica_data_valida("Digite a data: ")
        self.listar_transf(transf)

    def excluir_transf(self):
        self.listar_transfs()
        id_transf = self.__tela_transf.le_id("transferência")
        transf = self.pega_transf_por_id(id_transf)
        g1 = transf.funcionario
        contrato_g1 = self.__control_filial.control_contrato.pega_contrato_por_cpf_auto(g1.cpf)
        if (transf.funcionario.cargo.titulo != "Gerente"):
            contrato_g1.rem_transferencia(transf)
        else:
            op = self.__tela_transf.opcao_gerente()
            g2 = transf.filial_antiga.gerente
            contrato_g2 = self.__control_filial.control_contrato.pega_contrato_por_cpf_auto(g2.cpf)
            if (op == 1):
                contrato_g1.rem_transferencia(transf)
                transf.filial_antiga.gerente = g2
            else:
                self.__control_filial.control_contrato.finalizar_contrato(contrato_g2)
                contrato_g1.rem_transferencia(transf)
                self.__control_filial.control_mud_cargo.incluir_mud_cargo()
        self.__tela_transf.exclui_id(id_transf)
        self.__transferencias.remove(transf)

    def listar_transfs(self):
        if (len(self.__transferencias) == 0):
            self.__tela_transf.mostra_mensagem("\nNenhuma transferência realizada até o momento.")
        for transf in self.__transferencias:
            self.__tela_transf.mostra_transf({"id": transf.id, "funcionario": transf.funcionario.nome, "filial_antiga":
                                              transf.filial_antiga, "filial_nova": transf.filial_nova, "data": transf.data})

    def listar_transf(self, transf: Transferencia):
        self.__tela_transf.mostra_transf({"id": transf.id, "funcionario": transf.funcionario.nome, "filial_antiga":
                                          transf.filial_antiga, "filial_nova": transf.filial_nova, "data": transf.data})

    def listar_transf_por_data(self):
        mes = 0
        for transf in self.__transferencias:
            if (transf.data.month != mes):
                mes = transf.data.month
                self.__tela_transf.mostra_mensagem("\n" + transf.data.strftime("%m/%Y"))
            self.listar_transf(transf)

    def pega_transf_por_id(self, id: int):
        for transferencia in self.__transferencias:
            if (transferencia.id == id):
                return transferencia

    def retornar(self):
        self.__control_filial.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_transf, 2: self.alterar_transf, 3: self.excluir_transf, 4: self.listar_transfs,
                        5: self.listar_transf_por_data, 6: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_transf.mostra_opcoes()]()
