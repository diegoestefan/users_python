# API REST de Gerenciamento de Usuários

Esta é uma **API REST** simples para gerenciamento de usuários, construída com **Flask** e **MongoDB**. A API permite criar, listar, obter, atualizar e deletar usuários.  

A API também inclui **documentação Swagger** interativa para facilitar o uso e a integração.

## Funcionalidades

- **Criar Usuário**: Cadastrar um novo usuário com nome, e-mail e senha.
- **Listar Usuários**: Obter todos os usuários cadastrados.
- **Obter Usuário**: Consultar um usuário específico por ID.
- **Atualizar Usuário**: Modificar informações de um usuário existente.
- **Deletar Usuário**: Remover um usuário do banco de dados.
- **Documentação Swagger**: Acessível via navegador para testar e explorar os endpoints da API.

## Tecnologias Utilizadas

- **Flask** – Framework web para Python.
- **PyMongo** – Biblioteca para interagir com o MongoDB a partir de Python.
- **MongoDB** – Banco de dados NoSQL para armazenamento de dados.
- **Swagger** – Ferramenta para gerar documentação interativa da API.

## Requisitos

- **Python 3.0+**
- **MongoDB** instalado e rodando localmente na porta padrão (`27017`).

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt

3. Clone o repositório:

   ```bash
   python app.py

Agora a API estará disponível em http://127.0.0.1:5000/.

Acessando a Documentação Swagger:
Após iniciar o servidor, basta acessar a documentação interativa da API no seguinte endereço:

🔗 http://127.0.0.1:5000/docs
