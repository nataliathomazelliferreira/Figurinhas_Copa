from figurinha import Figurinha
from album import Album
from historico import Historico
from persistencia import Persistencia

class SistemaFigurinhas:
    def __init__(self):
        self.album = Album()
        self.historico = Historico()
        self.persistencia = Persistencia("dados.json")
        self.total_figurinhas = 670

    def ler_inteiro(self, mensagem):
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número válido.")
            return None

    def cadastrar_figurinha(self):
        id = self.ler_inteiro("Número da figurinha: ")

        if id is None:
            return

        if id <= 0:
            print("Número inválido.")
            return

        nome = input("Nome do jogador: ").strip()
        pais = input("Seleção: ").strip()
        posicao = input("Posição: ").strip()
        raridade = input("Raridade: ").strip()

        if nome == "" or pais == "" or posicao == "" or raridade == "":
            print("Todos os campos devem ser preenchidos.")
            return

        figurinha = Figurinha(id, nome, pais, posicao, raridade)
        self.album.adicionar(figurinha)

    def remover_figurinha(self):
        id = self.ler_inteiro("Número da figurinha para remover: ")

        if id is None:
            return

        self.album.remover(id)

    def consultar_por_numero(self):
        id = self.ler_inteiro("Número da figurinha: ")

        if id is None:
            return

        figurinha = self.album.buscar_por_id(id)

        if figurinha is None:
            print("Figurinha não encontrada.")
        else:
            print(figurinha.exibir())

    def consultar_por_jogador(self):
        nome = input("Nome do jogador: ").strip()
        self.album.buscar_por_nome(nome)

    def consultar_por_selecao(self):
        pais = input("Nome da seleção: ").strip()
        self.album.buscar_por_pais(pais)

    def ver_porcentagem(self):
        porcentagem = self.album.porcentagem_completa(self.total_figurinhas)
        print(f"Álbum concluído: {porcentagem:.2f}%")

    def registrar_troca(self):
        minha = self.ler_inteiro("Número da sua figurinha repetida: ")

        if minha is None:
            return

        recebida = self.ler_inteiro("Número da figurinha recebida: ")

        if recebida is None:
            return

        if not self.album.possui_repetida(minha):
            print("Você não possui essa figurinha repetida para trocar.")
            return

        nome = input("Nome do jogador recebido: ").strip()
        pais = input("Seleção do jogador recebido: ").strip()
        posicao = input("Posição do jogador recebido: ").strip()
        raridade = input("Raridade da figurinha recebida: ").strip()

        figurinha_trocada = self.album.remover_repetida(minha)

        nova_figurinha = Figurinha(recebida, nome, pais, posicao, raridade)
        self.album.adicionar(nova_figurinha)

        descricao = (
            f"Trocou a figurinha {figurinha_trocada.id} - {figurinha_trocada.nome} "
            f"pela figurinha {nova_figurinha.id} - {nova_figurinha.nome}"
        )

        self.historico.registrar_troca(descricao)
        print("Troca registrada com sucesso.")

    def mostrar_menu(self):
        print()
        print("===== ÁLBUM DE FIGURINHAS DA COPA =====")
        print("1 - Inserir figurinha")
        print("2 - Remover figurinha")
        print("3 - Consultar figurinha por número")
        print("4 - Consultar figurinha por jogador")
        print("5 - Consultar figurinha por seleção")
        print("6 - Ver álbum completo")
        print("7 - Ver porcentagem concluída")
        print("8 - Ver figurinhas repetidas")
        print("9 - Contar repetidas")
        print("10 - Registrar troca")
        print("11 - Ver histórico de trocas")
        print("12 - Salvar dados")
        print("13 - Carregar dados")
        print("0 - Sair")

    def executar(self):
        opcao = -1

        while opcao != 0:
            self.mostrar_menu()
            opcao = self.ler_inteiro("Escolha uma opção: ")

            if opcao is None:
                continue

            if opcao == 1:
                self.cadastrar_figurinha()
            elif opcao == 2:
                self.remover_figurinha()
            elif opcao == 3:
                self.consultar_por_numero()
            elif opcao == 4:
                self.consultar_por_jogador()
            elif opcao == 5:
                self.consultar_por_selecao()
            elif opcao == 6:
                self.album.mostrar_album()
            elif opcao == 7:
                self.ver_porcentagem()
            elif opcao == 8:
                self.album.mostrar_repetidas()
            elif opcao == 9:
                print(f"Quantidade de repetidas: {self.album.contar_repetidas()}")
            elif opcao == 10:
                self.registrar_troca()
            elif opcao == 11:
                self.historico.mostrar_historico()
            elif opcao == 12:
                self.persistencia.salvar(self.album, self.historico)
            elif opcao == 13:
                self.persistencia.carregar(self.album, self.historico)
            elif opcao == 0:
                print("Sistema encerrado.")
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    sistema = SistemaFigurinhas()
    sistema.executar()