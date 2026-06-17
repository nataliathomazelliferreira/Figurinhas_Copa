from nodos import NodoLista

class Album:
    def __init__(self):
        self.inicio = None
        self.repetidas = None
        self.total = 0
        self.total_repetidas = 0

    def adicionar(self, figurinha):
        if self.buscar_por_id(figurinha.id) is not None:
            self.adicionar_repetida(figurinha)
            print("Figurinha repetida adicionada.")
        else:
            novo = NodoLista(figurinha)
            novo.proximo = self.inicio
            self.inicio = novo
            self.total += 1
            print("Figurinha adicionada ao álbum.")

    def adicionar_repetida(self, figurinha):
        novo = NodoLista(figurinha)
        novo.proximo = self.repetidas
        self.repetidas = novo
        self.total_repetidas += 1

    def buscar_por_id(self, id):
        atual = self.inicio

        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha
            atual = atual.proximo

        return None

    def buscar_por_nome(self, nome):
        atual = self.inicio
        encontrou = False

        while atual is not None:
            if atual.figurinha.nome.lower() == nome.lower():
                print(atual.figurinha.exibir())
                encontrou = True
            atual = atual.proximo

        if not encontrou:
            print("Nenhuma figurinha encontrada.")

    def buscar_por_pais(self, pais):
        atual = self.inicio
        encontrou = False

        while atual is not None:
            if atual.figurinha.pais.lower() == pais.lower():
                print(atual.figurinha.exibir())
                encontrou = True
            atual = atual.proximo

        if not encontrou:
            print("Nenhuma figurinha encontrada.")

    def remover(self, id):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.figurinha.id == id:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                self.total -= 1
                print("Figurinha removida.")
                return

            anterior = atual
            atual = atual.proximo

        print("Figurinha não encontrada.")

    def mostrar_album(self):
        if self.inicio is None:
            print("Álbum vazio.")
            return

        atual = self.inicio

        while atual is not None:
            print(atual.figurinha.exibir())
            atual = atual.proximo

    def mostrar_repetidas(self):
        if self.repetidas is None:
            print("Nenhuma figurinha repetida.")
            return

        atual = self.repetidas

        while atual is not None:
            print(atual.figurinha.exibir())
            atual = atual.proximo

    def contar_repetidas(self):
        return self.total_repetidas

    def porcentagem_completa(self, total_figurinhas):
        return (self.total / total_figurinhas) * 100

    def possui_repetida(self, id):
        atual = self.repetidas

        while atual is not None:
            if atual.figurinha.id == id:
                return True
            atual = atual.proximo

        return False

    def remover_repetida(self, id):
        atual = self.repetidas
        anterior = None

        while atual is not None:
            if atual.figurinha.id == id:
                figurinha = atual.figurinha

                if anterior is None:
                    self.repetidas = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                self.total_repetidas -= 1
                return figurinha

            anterior = atual
            atual = atual.proximo

        return None

    def para_lista_dicionarios(self):
        dados = []
        atual = self.inicio

        while atual is not None:
            dados.append(atual.figurinha.para_dicionario())
            atual = atual.proximo

        return dados

    def repetidas_para_lista_dicionarios(self):
        dados = []
        atual = self.repetidas

        while atual is not None:
            dados.append(atual.figurinha.para_dicionario())
            atual = atual.proximo

        return dados