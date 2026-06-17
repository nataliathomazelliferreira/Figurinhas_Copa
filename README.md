# Sistema de Figurinhas da Copa

Projeto desenvolvido para a disciplina de Estrutura de Dados com o objetivo de implementar um sistema de gerenciamento de figurinhas da Copa do Mundo utilizando listas encadeadas e filas FIFO.

---

# Descrição do Projeto

O sistema simula um álbum de figurinhas da Copa do Mundo, permitindo que o usuário organize sua coleção, controle figurinhas repetidas, realize consultas, registre trocas e acompanhe o progresso do álbum.

O projeto foi desenvolvido aplicando conceitos fundamentais de Estrutura de Dados, sem utilizar estruturas prontas do Python para implementação da lista encadeada e da fila.

---

# Funcionalidades

O sistema permite:

* Inserir figurinha no álbum;
* Remover figurinha;
* Consultar figurinha por número;
* Consultar figurinha por jogador;
* Consultar figurinha por seleção;
* Visualizar o álbum completo;
* Verificar a porcentagem concluída do álbum;
* Armazenar figurinhas repetidas;
* Exibir a lista de figurinhas repetidas;
* Contar a quantidade de figurinhas repetidas;
* Registrar trocas de figurinhas;
* Visualizar o histórico de trocas;
* Salvar dados em arquivo JSON;
* Carregar dados previamente salvos.

---

# Estruturas de Dados Utilizadas

## Lista Encadeada

Utilizada para armazenar:

* Figurinhas do álbum;
* Figurinhas repetidas.

A implementação foi realizada através da classe `NodoLista`.

## Fila FIFO

Utilizada para armazenar:

* Histórico de trocas.

A implementação foi realizada através da classe `NodoFila`.

FIFO (First In, First Out) significa que o primeiro elemento inserido é o primeiro elemento removido.

---

# Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos
* Lista Encadeada
* Fila FIFO
* JSON
* Git
* GitHub

---

# Estrutura do Projeto

```text
Figurinhas_Copa/
│
├── main.py
├── figurinha.py
├── nodos.py
├── album.py
├── fila.py
├── historico.py
├── persistencia.py
├── dados.json
├── .gitignore
└── README.md
```

---

# Descrição dos Arquivos

| Arquivo         | Responsabilidade                                  |
| --------------- | ------------------------------------------------- |
| main.py         | Controle principal do sistema e menu de interação |
| figurinha.py    | Classe Figurinha                                  |
| nodos.py        | Classes NodoLista e NodoFila                      |
| album.py        | Implementação do álbum utilizando lista encadeada |
| fila.py         | Implementação da fila FIFO                        |
| historico.py    | Gerenciamento do histórico de trocas              |
| persistencia.py | Salvamento e carregamento dos dados               |
| dados.json      | Armazenamento das informações do sistema          |
| .gitignore      | Arquivos ignorados pelo Git                       |
| README.md       | Documentação do projeto                           |

---

# Observação

As estruturas de dados utilizadas neste projeto foram implementadas manualmente utilizando nós encadeados.

Não foram utilizadas estruturas prontas do Python para representar a lista encadeada e a fila FIFO exigidas pelo projeto.

---

# Como Baixar o Projeto

## Passo 1 – Abrir um Terminal

Abra um dos seguintes terminais:

* Prompt de Comando (CMD);
* PowerShell;
* Terminal integrado do VS Code.

---

## Passo 2 – Escolher a Pasta onde Deseja Salvar o Projeto

Navegue até a pasta onde deseja armazenar o projeto.

Exemplos:

```bash
cd Desktop
```

ou

```bash
cd Documentos
```

Você pode utilizar qualquer outro diretório de sua preferência.

---

## Passo 3 – Clonar o Repositório

Execute o comando abaixo:

```bash
git clone https://github.com/nataliathomazelliferreira/Figurinhas_Copa.git
```

O Git criará automaticamente uma pasta chamada:

```text
Figurinhas_Copa
```

e fará o download de todos os arquivos do projeto.

---

## Passo 4 – Entrar na Pasta do Projeto

Após finalizar o download, execute:

```bash
cd Figurinhas_Copa
```

Agora você estará dentro da pasta do projeto.

---

# Como Executar o Projeto

Com o terminal aberto dentro da pasta do projeto, execute:

```bash
python main.py
```

Caso seu sistema utilize o comando `python3`, execute:

```bash
python3 main.py
```

---

# Menu Principal

Ao iniciar o sistema será exibido um menu semelhante ao seguinte:

```text
1 - Inserir figurinha
2 - Remover figurinha
3 - Buscar por número
4 - Buscar por jogador
5 - Buscar por seleção
6 - Mostrar álbum
7 - Porcentagem concluída
8 - Mostrar repetidas
9 - Contar repetidas
10 - Registrar troca
11 - Histórico de trocas
12 - Salvar dados
13 - Carregar dados
0 - Sair
```

---

# Persistência dos Dados

O sistema utiliza um arquivo JSON para armazenar as informações do álbum.

Ao selecionar a opção:

```text
12 - Salvar dados
```

os dados serão gravados no arquivo:

```text
dados.json
```

Para recuperar informações previamente salvas, utilize:

```text
13 - Carregar dados
```

Serão restauradas:

* Figurinhas do álbum;
* Figurinhas repetidas;
* Histórico de trocas.

---

# Atualizando o Projeto no GitHub

Após realizar alterações no código, utilize os seguintes comandos:

```bash
git add .
git commit -m "Descrição da alteração"
git push
```

## Explicação dos Comandos

### git add .

Adiciona todos os arquivos modificados para preparação do commit.

### git commit -m "Descrição da alteração"

Cria um registro permanente das alterações realizadas.

### git push

Envia as alterações para o repositório remoto no GitHub.

---

# Objetivos de Aprendizagem

Este projeto foi desenvolvido com o objetivo de aplicar conceitos de:

* Programação Orientada a Objetos;
* Classes e Objetos;
* Lista Encadeada;
* Fila FIFO;
* Manipulação de Arquivos JSON;
* Modularização de Código;
* Estruturas de Dados.

---

# Status do Projeto

Projeto desenvolvido para fins acadêmicos na disciplina de Estrutura de Dados da Faculdade de Tecnologia de Rio Claro (FATEC).  