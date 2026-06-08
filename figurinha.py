class Figurinha:
    def __init__(self, id, nome, pais, posicao, raridade):
        self.id = id
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

    def exibir(self):
        return f"{self.id} - {self.nome} | {self.pais} | {self.posicao} | {self.raridade}"

    def para_dicionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "pais": self.pais,
            "posicao": self.posicao,
            "raridade": self.raridade
        }

    @staticmethod
    def de_dicionario(dados):
        return Figurinha(
            dados["id"],
            dados["nome"],
            dados["pais"],
            dados["posicao"],
            dados["raridade"]
        )