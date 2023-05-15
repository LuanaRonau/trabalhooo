from entidade.filial import Filial
from entidade.gerente import Gerente
from controladores.controlador_filial import ControladorFilial
from controladores.controlador_gerente import ControladorGerente
from controladores.controlador_fun_comum import ControladorFunComum
from controladores.controlador_contrato import ControladorContrato
from telas.tela_sistema import TelaSistema
from exception.repeticao import Repeticao
from exception.naoExistencia import NaoExistencia
from datetime import date
from controladores.controlador_cargo import ControladorCargo
from controladores.controlador_transf import ControladorTransf
from controladores.controlador_mud_cargo import ControladorMudCargo


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_gerente = ControladorGerente()
        self.__controlador_contrato = ControladorContrato(self)
        self.__controlador_fun_comum = ControladorFunComum()
        self.__controlador_cargo = ControladorCargo(self)
        self.__controlador_transf = ControladorTransf(self)
        self.__controlador_mud_cargo = ControladorMudCargo(self)
        self.__lista_filiais = []

    @property
    def controlador_contrato(self):
        return self.__controlador_contrato

    @property
    def controlador_transf(self):
        return self.__controlador_transf

    @property
    def controlador_mud_cargo(self):
        return self.__controlador_mud_cargo

    @property
    def controlador_gerente(self):
        return self.__controlador_gerente

    @property
    def controlador_fun_comum(self):
        return self.__controlador_fun_comum

    @property
    def controlador_cargo(self):
        return self.__controlador_cargo

    def inicializa_sistema(self):
        lista_opcoes = {1: self.adicionar_filial, 2: self.excluir_filial,
                        3: self.modificar_filial, 4: self.listar_por_atv,
                        5: self.gerenciamento_cargos, 0: self.sair}

        while True:
            opcao_escolhida = self.__tela_sistema.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def adicionar_filial(self):
        while True:
            self.__tela_sistema.mostra_mensagem("\n=== Tela cadastro de filial ===")
            dados_nova_filial = self.__tela_sistema.pega_dados_cadastro()
            # Checagem de repetição
            if self.checagem_repeticao_cep(dados_nova_filial['cep']):
                if self.checagem_repeticao_cep(dados_nova_filial['cep']):
                    break

        infos_gerencia = self.__controlador_gerente.add_gerente()
        nova_filial = Filial(dados_nova_filial['cep'], dados_nova_filial['cidade'], infos_gerencia['funcionario'])
        self.__lista_filiais.append(nova_filial)

        dados_contrato = {'data_inicio': infos_gerencia['data_inicio'], 'cargo': infos_gerencia['cargo'],
                          'empregado': infos_gerencia['funcionario'], 'filial': nova_filial,
                          'empregador': infos_gerencia['empregador'], 'id': infos_gerencia['id']}
        self.__controlador_contrato.incluir_contrato(dados_contrato)

        self.__tela_sistema.mostra_mensagem('Filial cadastrada com sucesso.')

    def excluir_filial(self):
        self.__tela_sistema.mostra_mensagem('\n=== EXCLUSÃO DE FILIAIS ===\nRealize a busca.')
        filial = self.busca_por_cep("CEP: ")
        self.__lista_filiais.remove(filial)
        self.__tela_sistema.mostra_mensagem('Filial excluída com sucesso.')

    def modificar_filial(self):
        self.__tela_sistema.mostra_mensagem('\n=== Modificação filial por CEP ===')
        filial = self.busca_por_cep("Digite o CEP: ")
        ControladorFilial(self, self.__controlador_contrato, filial).inicializa_sistema()

    def listar_por_atv(self):
        if len(self.__lista_filiais) > 0:
            self.__tela_sistema.mostra_mensagem("\n=== Listagem de filiais ===\n")
            for _ in self.__lista_filiais:
                self.__tela_sistema.listagem(_.cep, _.cidade, _.gerente.nome)
        else:
            self.__tela_sistema.mostra_mensagem('Lista vazia.\n')

    # Método de checagem de repetição
    def checagem_repeticao_cep(self, cep):
        try:
            for _ in self.__lista_filiais:
                if _.cep == cep:
                    Repeticao('CEP', cep).msg()
                    raise Repeticao('CEP', cep)
            return True
        except Repeticao:
            return False

    def checagem_repeticao_cidade(self, cidade):
        try:
            for _ in self.__lista_filiais:
                if _.cidade == cidade:
                    Repeticao('Cidade', cidade).msg()
                    raise Repeticao('Cidade', cidade)
            return True
        except Repeticao:
            return False

    def busca_por_cep(self, msg):
        while True:
            cep_buscado = self.__tela_sistema.le_cep(msg)
            try:
                for _ in self.__lista_filiais:
                    if _.cep == cep_buscado:
                        return _
                raise NaoExistencia
            except NaoExistencia:
                print('Filial não encontrada. Tente novamente.')

    def gerenciamento_cargos(self):
        self.__controlador_cargo.abre_tela()

    def sair(self):
        exit(0)
