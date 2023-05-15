from telas.tela_gerente import TelaGerente
from entidade.gerente import Gerente
from entidade.cargo import Cargo
from exception.repeticao import Repeticao
from datetime import date
from exception.naoExistencia import NaoExistencia

class ControladorGerente:

    def __init__(self):
        self.__tela_gerente = TelaGerente()
        self.__gerentes = [Gerente("Empresa", "999", date(1999, 6, 7))]
        self.__gerentes_cargos = [Cargo(0, 'Gerente', 10000)]

    def add_gerente(self, novo_gerente=None):
        if novo_gerente == None:
            self.__tela_gerente.mostra_mensagem("\n=== Cadastro de gerente ===")
            # Realizando a checagem de repetição de CPF
            while True:
                novo_gerente = self.__tela_gerente.pega_dados_cadastro()
                if self.checagem_repeticao(novo_gerente['CPF']):
                    break
                self.__tela_gerente.mostra_mensagem('CPF já cadastrado.')
        self.__gerentes.append(Gerente(novo_gerente['nome'], novo_gerente['CPF'], novo_gerente['data_nasc']))
        id = self.__tela_gerente.gera_id()
        # Infomações constantes para todos os gerentes
        infos_gerencia = {'funcionario': self.__gerentes[-1], 'empregador': self.__gerentes[0], 'id': id,
                          'cargo': self.__gerentes_cargos[0], 'data_inicio': novo_gerente['data_inicio']}
        return infos_gerencia

    def checagem_repeticao(self, cpf):
        while True:
            try:
                for _ in self.__gerentes:
                    if _.cpf == cpf:
                        raise Repeticao('CPF', cpf)
                return True
            except Repeticao:
                return False
