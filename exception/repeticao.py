class Repeticao(Exception):
    def __init__(self, obj_repetido, valor_repetido):
        super().__init__(f"Repetição não permetida em '{obj_repetido}': {valor_repetido}")