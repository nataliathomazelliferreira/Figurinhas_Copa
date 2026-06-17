from fila import Fila

class Historico:
    def __init__(self):
        self.fila = Fila()

    def registrar_troca(self, descricao):
        self.fila.enqueue(descricao)

    def mostrar_historico(self):
        self.fila.mostrar()

    def para_lista(self):
        return self.fila.para_lista()

    def carregar_historico(self, dados):
        for item in dados:
            self.fila.enqueue(item)