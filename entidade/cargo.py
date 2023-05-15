class Cargo:
    def __init__(self, id: int, titulo: str, salario: int):
        self.__id = id
        self.__titulo = titulo
        self.__salario = salario

    @property
    def id(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def salario(self):
        return self.__salario

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @salario.setter
    def salario(self, salario: int):
        if isinstance(salario, int):
            self.__salario = salario
