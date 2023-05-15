from telas.tela_funcionarios import TelaFuncionario


class TelaGerente(TelaFuncionario):

    def __init__(self):
        super().__init__()

    def mostra_mensagem(self, msg):
        super().mostra_mensagem(msg)

    def mostra_opcoes(self):
        print("\nTELA DE MODIFICAÇÃO: GERENTE\n"
              + "1) Modificar informações do gerente atual\n"
              + "2) Demitir \n"
              + "3) Transferir \n"
              + "4) Mudar cargo \n"
              + "5) Listagem de contratos realizados\n"
              + "6) Acessar contrato\n"
              + "0) Retornar\n")
        opcao = super().le_int_validos([1, 2, 3, 4, 5, 6, 7, 0], "Escolha uma opçao: ")
        return opcao

    def menu_nova_gerencia(self):
        op_novo_gerente = input("Informe o próximo gerente:"
                                + "1) Promover funcionário"
                                + "2) Cadastrar novo gerente")
        return op_novo_gerente
