from nodos import NodoFila

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enqueue(self, valor):
        novo = NodoFila(valor)

        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    def dequeue(self):
        if self.inicio is None:
            return None

        valor = self.inicio.valor
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return valor

    def peek(self):
        if self.inicio is None:
            return None

        return self.inicio.valor

    def limpar(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def mostrar(self):
        if self.inicio is None:
            print("Fila vazia.")
            return

        atual = self.inicio

        while atual is not None:
            print(atual.valor)
            atual = atual.proximo

    def para_lista(self):
        dados = []
        atual = self.inicio

        while atual is not None:
            dados.append(atual.valor)
            atual = atual.proximo

        return dados