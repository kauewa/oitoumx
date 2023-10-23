class Etapas:
    def __init__(self, nome:str) -> None:
        self.nome = nome

class Championchip:
    def __init__(self, nome:str, etapas:Etapas) -> None:
        self.nome = nome
        self.etapas = etapas