from abc import ABC, abstractmethod
from datetime import datetime, date
from exception.negativeValueException import NegativeValueException
from exception.opcao_invalida import OpcaoInvalida

class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_mensagem(self, msg):
        print(msg)

    def pega_input(self, msg: str):
        inp = input(msg)
        return inp

    def le_cpf(self, msg):
        while True:
            print('Formatação CPF válido: 13255870950 (11 ints)')
            cpf = input(msg)
            try:
                if len(cpf) == 11:
                    f1 = cpf[:3]
                    f2 = cpf[3:6]
                    f3 = cpf[6:9]
                    f4 = cpf[9:]
                    return f'{f1}.{f2}.{f3}-{f4}'
                else:
                    raise ValueError
            except ValueError:
                print('CPF inválido')

    def le_int_validos(self, int_validos: list, msg):
        while True:
            variavel = input(msg)
            try:
                opcao = int(variavel)
                if opcao not in int_validos:
                    raise OpcaoInvalida
                return opcao
            except ValueError:
                print('Esse valor deve ser um inteiro.')
            except OpcaoInvalida:
                print('Digite uma opção disponível.')

    def le_intervalo(self, menor_valor, maior_valor, msg):
        while True:
            variavel = input(msg)
            try:
                opcao = int(variavel)
                if menor_valor <= opcao <= maior_valor:
                    return opcao
                else:
                    raise OpcaoInvalida
            except ValueError:
                print('Esse valor deve ser um inteiro.')
            except OpcaoInvalida:
                print('Digite uma opção disponível.')

    def le_int_positivo(self, msg):
        while True:
            variavel = input(msg)
            try:
                variavel_int = int(variavel)
                if variavel_int < 0:
                    raise NegativeValueException
                return variavel_int
            except ValueError:
                print('Esse valor deve ser um inteiro.')
            except NegativeValueException:
                print('Esse valor deve ser positivo.')

    def le_cep(self, msg: str):
        while True:
            try:
                cep = input(msg)
                if len(cep) != 9:
                    raise ValueError
                if cep[5] != "-":
                    raise ValueError
                parte_a = cep[:5]
                parte_b = cep[6:]
                int(parte_a)
                int(parte_b)
                return cep
            except ValueError:
                print("\nCEP inválido, talvez você está digitando fora do formato desejado")

    def le_data(self, msg: str):
        while True:
            try:
                data = input(msg)
                data = datetime.strptime(data, "%d/%m/%Y").date()
                if (date.today() < data):
                    raise ValueError
                return data
            except ValueError:
                print("\nData incorreta ou fora do formato desejado")

    def gera_id(self):
        pass

    def exclui_id(self, id: int):
        pass

    def le_id(self, tipo: str):
        pass