from telas.tela_gerente import TelaGerente


class ControladorGerenteEsp:

    def __init__(self, controlador_filial, controlador_contrato, controlador_sistema, gerente):
        self.__controlador_filial = controlador_filial
        self.__controlador_contrato = controlador_contrato
        self.__controlador_sistema = controlador_sistema
        self.__tela_gerente = TelaGerente()
        self.__gerente = gerente

    def inicializa_sistema(self):
        lista_opcoes = {1: self.modificar_dados, 2: self.demitir,
                        3: self.transferir, 4: self.mudar_cargo,
                        5: self.listar_contratos, 6: self.acessar_contrato,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_gerente.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def gerente(self, gerente):
        self.__gerente = gerente

    def modificar_dados(self):
        self.__tela_gerente.mostra_mensagem('\n=== Modificação de dados ===')
        opcao = self.__tela_gerente.menu_modificacao()
        if opcao == 1:
            novo_nome = self.__tela_gerente.pega_input("Digite o novo nome:")
            self.__gerente.nome = novo_nome
        if opcao == 2:
            novo_cpf = self.__tela_gerente.pega_input("Digite o novo CPF:")
            self.__gerente.cpf = novo_cpf
        if opcao == 3:
            nova_data_nasc = self.__tela_gerente.pega_input("Digite a nova data de nascimento:")
            self.__gerente.data_nasc = nova_data_nasc
        if opcao == 0:
            return

    def demitir(self):
        pass

    def transferir(self):
        pass

    def mudar_cargo(self):
        pass

    def listar_contratos(self):
        if len(self.__gerente.contratos) > 0:
            for contrato in self.__gerente.contratos:
                self.__controlador_contrato.tela_contrato.listar_contrato(contrato)

    def acessar_contrato(self):
        self.__controlador_contrato.inicializa_sistema(self, self.__gerente)

    def retornar(self):
        self.__controlador_filial.inicializa_sistema()
