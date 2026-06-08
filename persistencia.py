import json
from figurinha import Figurinha


class Persistencia:
    def __init__(self, caminho):
        self.caminho = caminho

    def salvar(self, album, historico):
        dados = {
            "album": album.para_lista_dicionarios(),
            "repetidas": album.repetidas_para_lista_dicionarios(),
            "historico": historico.para_lista()
        }

        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

        print("Dados salvos com sucesso.")

    def carregar(self, album, historico):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            for item in dados["album"]:
                figurinha = Figurinha.de_dicionario(item)
                album.adicionar(figurinha)

            for item in dados["repetidas"]:
                figurinha = Figurinha.de_dicionario(item)
                album.adicionar_repetida(figurinha)

            historico.carregar_historico(dados["historico"])

            print("Dados carregados com sucesso.")

        except FileNotFoundError:
            print("Arquivo de dados não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")