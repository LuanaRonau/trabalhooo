from datetime import datetime, date

# data = input("data no formato ...: ")
#
# #dia, mes, ano = teclado.split("/")
#
# def verifica_data_valida(data: str):
#     while True:
#         try:
#             data = datetime.strptime(data, "%d/%m/%Y").date()
#             if (date.today() < data):
#                 raise ValueError
#             return data
#         except ValueError:
#             print("Data incorreta ou fora do formato desejado [dia/mes/ano]: ")
#             data = input("Digite a data novamente: (exemplo: 14/04/2023) ")
#
#
# print(verifica_data_valida(data))

# data_inicio = date(2023, 5, 31)
#
# print(data_inicio.month)

# teclado = input()
# if teclado[5] != "-":
#     print("error")
#
# parteA = teclado[:5]
# parteB = teclado[6:]
#
# print(len(parteA))
hoje = date.today()
print(int(hoje - date(2004, 5, 3))
