from nodos import NodoLista


class Album:
    def __init__(self):
        self.cabeca = None
        self.repetidas = None
        self.tamanho = 0
        self.qtd_repetidas = 0

    def adicionar(self, figurinha):
        if self.buscar_por_id(figurinha.id) is not None:
            self.adicionar_repetida(figurinha)
            print("Figurinha repetida adicionada à lista de repetidas.")
            return

        novo = NodoLista(figurinha)

        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo

        self.tamanho += 1
        print("Figurinha adicionada ao álbum.")

    def adicionar_repetida(self, figurinha):
        novo = NodoLista(figurinha)

        if self.repetidas is None:
            self.repetidas = novo
        else:
            atual = self.repetidas
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo

        self.qtd_repetidas += 1

    def remover(self, id):
        atual = self.cabeca
        anterior = None

        while atual is not None:
            if atual.figurinha.id == id:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                self.tamanho -= 1
                print("Figurinha removida.")
                return True

            anterior = atual
            atual = atual.proximo

        print("Figurinha não encontrada.")
        return False

    def buscar_por_id(self, id):
        atual = self.cabeca

        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha
            atual = atual.proximo

        return None

    def buscar_por_nome(self, nome):
        atual = self.cabeca
        encontrou = False

        while atual is not None:
            if atual.figurinha.nome.lower() == nome.lower():
                print(atual.figurinha.exibir())
                encontrou = True
            atual = atual.proximo

        if not encontrou:
            print("Nenhuma figurinha encontrada com esse nome.")

    def buscar_por_pais(self, pais):
        atual = self.cabeca
        encontrou = False

        while atual is not None:
            if atual.figurinha.pais.lower() == pais.lower():
                print(atual.figurinha.exibir())
                encontrou = True
            atual = atual.proximo

        if not encontrou:
            print("Nenhuma figurinha encontrada dessa seleção.")

    def mostrar_album(self):
        if self.cabeca is None:
            print("Álbum vazio.")
            return

        atual = self.cabeca

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
        return self.qtd_repetidas

    def porcentagem_completa(self, total_figurinhas):
        if total_figurinhas <= 0:
            return 0

        return (self.tamanho / total_figurinhas) * 100

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

                self.qtd_repetidas -= 1
                return figurinha

            anterior = atual
            atual = atual.proximo

        return None

    def para_lista_dicionarios(self):
        dados = []
        atual = self.cabeca

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