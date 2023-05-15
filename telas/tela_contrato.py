from telas.abstract_tela import AbstractTela
from exception.naoExistencia import NaoExistencia

class TelaContrato(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__id_gerados = []

    def mostra_opcoes(self):
        opcao = input("\nTela de gerenciamento dos contratos"
                      "\n1) Registrar contrato"
                      "\n2) Alterar contrato"
                      "\n3) Excluir contrato"
                      "\n4) Listar todos os contratos"
                      "\n5) Gerar relatório de contratos por data de realização"
                      "\n6) Listar histórico de um funcionário"
                      "\n7) Finalizar contrato"
                      "\n8) Retornar para tela do sistema")
        self.le_int_validos([1, 2, 3, 4, 5, 6, 7, 8], "\nDigite a opção do menu que deseja: ")
        return opcao
        
    def pega_dados_contrato(self, id=None):
        print("\n~~~~~~~~  Preenchendo um contrato  ~~~~~~~~")
        cep = super().le_cep("Digite o CEP da filial no formato XXXXX-XXX: ")
        data_inicio = super().le_data("Digite a data de início do contrato no formato dia/mês/ano: "
                                                "(exemplo: 15/05/2023) ")
        empregado = super().le_cpf("Digite o CPF da pessoa contratada: ")
        if (id == None):
            id = self.gera_id()

        return {"cep": cep, "data_inicio": data_inicio, "empregado": empregado, "id": id}

    def mostra_contrato(self, dados_contrato):
        print(f"\nContrato de identificação: {dados_contrato['id']}"
              f"\n   Por meio deste contrato o(a) contratante {dados_contrato['empregador']} contrata o(a) "
              f"funcionário(a) {dados_contrato['empregado']} para exercer o cargo de {dados_contrato['cargo']}."
              f"\n{dados_contrato['filial']}, {dados_contrato['data'].strftime('%d/%m/%Y')}")

    def le_id(self, tipo: str):
        while True:
            try:
                id = int(input(f"\nEscolha qual {tipo} digitando seu identificador: "))
                if (id not in self.__id_gerados):
                    raise NaoExistencia()
                return id
            except NaoExistencia:
                print(f"Não foi encontrado(a) nenhum(a) {tipo} com essa identificação.")

    def gera_id(self):
        if len(self.__id_gerados) > 0:
            novo_id = (self.__id_gerados[-1] + 1)
            self.__id_gerados.append(novo_id)
            return novo_id
        else:
            return 0

    def exclui_id(self, id: int):
        self.__id_gerados.remove(id)

    def mostra_mensagem(self, msg):
        super().mostra_mensagem(msg)


