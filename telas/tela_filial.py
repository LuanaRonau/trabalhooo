from telas.abstract_tela import AbstractTela


class TelaFilial(AbstractTela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print(f"\nTELA DE MODIFICAÇÃO: FILIAL\n"
              + "O que deseja fazer?\n"
              + "1) Acessar opções de funcionários comuns\n"
              + "2) Acessar opções de gerencia\n"
              + "3) Acessar opções de contratos\n"
              + "4) Acessar opções de transferência\n"
              + "5) Acessar opções de mudança de cargo\n"
              + "6) Modificar dados da filial\n"
              + "7) Acessar registros de ocorrencias\n"
              + "8) Acessar funcionários por atividade\n"
              + "0) Retornar\n")
        opcao = super().le_int_validos([0, 1, 2, 3, 4, 5, 6, 7, 8], "Escolha uma opção: ")
        return opcao

    def menu_modificacao(self):
        print("O que deseja modificar?\n"
              + "(Para demais modificações, consulte as outras opções do menu.)\n"
              + "1) CEP\n"
              + "2) Cidade\n"
              + "0) Retornar\n")
        opcao = super().le_int_validos([1, 2, 0], "Escolha uma opçao: ")
        return opcao

    def listagem(self, nome, cpf, data_nasc):
        print(f"Nome: {nome}\nCPF: {cpf}\nData_nasc: {data_nasc}\n")

    def mostra_mensagem(self, msg):
        super().mostra_mensagem(msg)
