from telas.abstract_tela import AbstractTela
from exception.naoExistencia import NaoExistencia


class TelaMudCargo(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__id_gerados = []

    def mostra_opcoes(self):
        print("\nTela de gerenciamento das mudanças de cargos"
                      "\n1) Registrar mudança de cargo"
                      "\n2) Alterar mudança de cargo"
                      "\n3) Excluir mudança de cargo"
                      "\n4) Listar todas as mudanças de cargos"
                      "\n5) Listar mudanças de cargos por data de realização"
                      "\n6) Retornar")
        return super().le_int_validos([1, 2, 3, 4, 5, 6], "Digite a opção do menu que deseja: ")
        
    def pega_dados_mud_cargo(self, id=None):
        print("\n~~~~~~~~ Inserindo os dados da mudança de cargo ~~~~~~~~")
        if id == None:
            super().gera_id()
        cpf = super().le_cpf("Digite apenas os números do CPF do funcionário que será transferido de filial: ")
        data = super().le_data("Digite a data da transferência no formato dia/mês/ano: (exemplo: 31/03/2023) ")
        promocao = 0
        while promocao != "S" and promocao != "N":
            promocao = input("O funcionario está sendo promovido a gerente? [S/N] ").upper()

        return {"data": data, "cpf": cpf, "id": id, "promocao": promocao}

    def mostra_mud_cargo(self, dados_mud_cargo):
        print(f"\nIdentificação: {dados_mud_cargo['id']}"
              f"\nFuncionario: {dados_mud_cargo['funcionario']}"
              f"\nCargo antigo: {dados_mud_cargo['cargo_antigo']}"
              f"\nCargo novo: {dados_mud_cargo['cargo_novo']}"
              f"\nData: {dados_mud_cargo['data']}")

    def mostra_mensagem(self, msg):
        super().mostra_mensagem(msg)

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