from figurinha import Figurinha
from album import Album
from historico import Historico
from persistencia import Persistencia

def menu():
    print("\n===== ÁLBUM DA COPA =====")
    print("1 - Inserir figurinha")
    print("2 - Remover figurinha")
    print("3 - Buscar por número")
    print("4 - Buscar por jogador")
    print("5 - Buscar por seleção")
    print("6 - Mostrar álbum")
    print("7 - Porcentagem concluída")
    print("8 - Mostrar repetidas")
    print("9 - Contar repetidas")
    print("10 - Registrar troca")
    print("11 - Histórico de trocas")
    print("12 - Salvar dados")
    print("13 - Carregar dados")
    print("0 - Sair")

def ler_numero(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        print("Número inválido.")
        return None

def inserir_figurinha(album):
    numero = ler_numero("Número da figurinha: ")

    if numero is None:
        return

    if numero <= 0:
        print("O número da figurinha deve ser maior que zero.")
        return

    nome = input("Nome do jogador: ").strip()
    pais = input("Seleção: ").strip()
    posicao = input("Posição: ").strip()
    raridade = input("Raridade: ").strip()

    if nome == "" or pais == "" or posicao == "" or raridade == "":
        print("Todos os campos devem ser preenchidos.")
        return

    figurinha = Figurinha(numero, nome, pais, posicao, raridade)
    album.adicionar(figurinha)

def remover_figurinha(album):
    numero = ler_numero("Número da figurinha para remover: ")

    if numero is None:
        return

    album.remover(numero)

def buscar_por_numero(album):
    numero = ler_numero("Número da figurinha: ")

    if numero is None:
        return

    figurinha = album.buscar_por_id(numero)

    if figurinha is None:
        print("Figurinha não encontrada.")
    else:
        print(figurinha.exibir())

def buscar_por_jogador(album):
    nome = input("Nome do jogador: ").strip()

    if nome == "":
        print("Digite um nome válido.")
        return

    album.buscar_por_nome(nome)

def buscar_por_selecao(album):
    pais = input("Nome da seleção: ").strip()

    if pais == "":
        print("Digite uma seleção válida.")
        return

    album.buscar_por_pais(pais)

def registrar_troca(album, historico):
    minha = ler_numero("Número da sua figurinha repetida: ")

    if minha is None:
        return

    recebida = ler_numero("Número da figurinha recebida: ")

    if recebida is None:
        return

    if not album.possui_repetida(minha):
        print("Você não possui essa figurinha repetida.")
        return

    nome = input("Nome do jogador recebido: ").strip()
    pais = input("Seleção do jogador recebido: ").strip()
    posicao = input("Posição do jogador recebido: ").strip()
    raridade = input("Raridade da figurinha recebida: ").strip()

    if nome == "" or pais == "" or posicao == "" or raridade == "":
        print("Todos os campos devem ser preenchidos.")
        return

    figurinha_entregue = album.remover_repetida(minha)
    figurinha_recebida = Figurinha(recebida, nome, pais, posicao, raridade)

    album.adicionar(figurinha_recebida)

    descricao = (
        f"Troca realizada: entregou {figurinha_entregue.id} - "
        f"{figurinha_entregue.nome} e recebeu {figurinha_recebida.id} - "
        f"{figurinha_recebida.nome}"
    )

    historico.registrar_troca(descricao)

    print("Troca registrada com sucesso.")

def executar():
    album = Album()
    historico = Historico()
    persistencia = Persistencia("dados.json")
    total_figurinhas = 670

    opcao = -1

    while opcao != 0:
        menu()
        opcao = ler_numero("Escolha uma opção: ")

        if opcao is None:
            continue

        if opcao == 1:
            inserir_figurinha(album)

        elif opcao == 2:
            remover_figurinha(album)

        elif opcao == 3:
            buscar_por_numero(album)

        elif opcao == 4:
            buscar_por_jogador(album)

        elif opcao == 5:
            buscar_por_selecao(album)

        elif opcao == 6:
            album.mostrar_album()

        elif opcao == 7:
            porcentagem = album.porcentagem_completa(total_figurinhas)
            print(f"Álbum concluído: {porcentagem:.2f}%")

        elif opcao == 8:
            album.mostrar_repetidas()

        elif opcao == 9:
            print(f"Quantidade de repetidas: {album.contar_repetidas()}")

        elif opcao == 10:
            registrar_troca(album, historico)

        elif opcao == 11:
            historico.mostrar_historico()

        elif opcao == 12:
            persistencia.salvar(album, historico)

        elif opcao == 13:
            persistencia.carregar(album, historico)

        elif opcao == 0:
            print("Sistema encerrado.")

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    executar()