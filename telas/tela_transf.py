from telas.abstract_tela import AbstractTela
from exception.naoExistencia import NaoExistencia


class TelaTransf(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__id_gerados = []

    def mostra_opcoes(self):
        print("\nTela de gerenciamento de transferências"
              "\n1 - Registrar transferência"
              "\n2 - Alterar transferência"
              "\n3 - Excluir transferência"
              "\n4 - Listar todas as transferências"
              "\n5 - Listar transferências por data de realização"
              "\n6 - Retornar")

        return super().le_int_validos([1, 2, 3, 4, 5, 6], "Digite a opção do menu que deseja: ")

    def pega_dados_transf(self, id=None):
        print("\n~~~~~~~~ Inserindo os dados da transferência ~~~~~~~~")
        cpf = super().le_cpf("Digite apenas os números do CPF do funcionário que será transferido de filial: ")
        if (id == None):
            id = super().gera_id()
        cep_filial_nova = super().le_cep("Digite o CEP da nova filial: [XXXXX-XXX] ")
        data = super().le_data("Digite a data da transferência no formato dia/mês/ano: (exemplo: 31/03/2023) ")

        return {"cpf": cpf, "id": id, "cep_filial_nova": cep_filial_nova, "data": data}

    def escolha_alteracao(self):
        print("\n1) Funcionário (apenas para funcionários comuns)"
              "\n2) Filial (apenas para funcionários comuns)"
              "\n3) Data")
        return super().le_int_validos([1, 2, 3], "Qual atributo você deseja alterar? ")

    def opcao_gerente(self):
        print("Não é possível deixar uma filial sem gerência, aqui estão as opções para evitar que isso aconteça:"
              "\n1) Trocar um gerente por outro gerente"
              "\n2) Demitir o gerente da nova filial e promover um funcionário em sua filial antiga")
        return super().le_int_validos([1, 2], "Digite a opção que deseja: ")

    def mostra_transf(self, dados_transf):
        print(f"\nIdentificação: {dados_transf['id']}"
              f"\nFuncionario: {dados_transf['funcionario']}"
              f"\nFilial antiga: {dados_transf['filial_antiga']}"
              f"\nFilial nova: {dados_transf['filial_nova']}"
              f"\nData: {dados_transf['data']}")

    def gera_id(self):
        if len(self.__id_gerados) > 0:
            novo_id = (self.__id_gerados[-1] + 1)
            self.__id_gerados.append(novo_id)
            return novo_id
        else:
            return 0

    def exclui_id(self, id: int):
        self.__id_gerados.remove(id)

    def le_id(self, tipo: str):
        while True:
            try:
                id = int(input(f"\nEscolha qual {tipo} digitando seu identificador: "))
                if (id not in self.__id_gerados):
                    raise NaoExistencia()
                return id
            except NaoExistencia:
                print(f"Não foi encontrado(a) nenhum(a) {tipo} com essa identificação.")

    def mostra_mensagem(self, msg: str):
        super().mostra_mensagem(msg)
