from telas.tela_funcionarios import TelaFuncionario

class TelaFuncomum(TelaFuncionario):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        print("\nTELA DE MODIFICAÇÃO: FUNCIONARIO COMUM\n"
              + "1) Modificar informações\n"
              + "2) Cadastrar novo funcionario comum\n"
              + "3) Demitir\n"
              + "4) Transferir \n"
              + "5) Mudar cargo \n"
              + "6) Acessar contrato\n"
              + "7) Listar todos\n"
              + "0) Retornar\n")
        opcao = super().le_int_validos([1, 2, 3, 4, 5, 6, 7, 0], "Escolha uma opçao: ")
        return opcao

    def pega_cpf(self, msg):
        return self.le_int_positivo(msg)

    def listagem(self, nome, cpf, data_nasc):
        print(f"Nome: {nome}\nCPF: {cpf}\nData_nasc: {data_nasc}\n")
