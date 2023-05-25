# Reserva de Mesas

Este projeto é uma aplicação web que serve como um sistema de reserva para um restaurante. Foi desenvolvido como um projeto para a disciplina de Programação Avançada da Faculdade FACAMP. A aplicação utiliza Vue.js no frontend, Flask no backend e MongoDB como o banco de dados NoSQL.

## Funcionalidades

A aplicação permite aos usuários:

1. Registrar uma nova conta.
2. Efetuar login em uma conta existente.
3. Realizar uma reserva.
4. Visualizar reservas existentes.

##Prints

![Tela de Login](https://i.imgur.com/NDQnQJo.png)

![Tela de Registro](https://i.imgur.com/z0bslSX.png)

![Tela Inicial](https://i.imgur.com/c3SgOrT.png)

![Tela de Edição](https://i.imgur.com/59xjoFA.png)

## Configuração do Projeto

Para configurar o projeto, siga as etapas a seguir:

### Pré-requisitos

- Python 3.7+
- MongoDB Atlas
- Node.js e npm

## Instalação

1. Clonar Repositório: 

```bash
git clone https://github.com/wolf-stievano/Trabalho_Semestral
cd Trabalho_Semestral
```

2. Crie e ative um ambiente virtual Python:

```bash
python -m venv .venv
source .venv/bin/activate (Linux/Mac)
.venv\Scripts\activate (Windows)
```

3. Instale as dependências do backend:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.ini` na raiz do projeto e adicione suas credenciais do MongoDB Atlas:

```
[PROD]
DB_URI = seu_uri_de_conexão_do_mongodb_atlas
```

5. Instale as dependências do frontend:

```bash
npm install
```

## Executando o projeto

1. Inicie o servidor backend:

```bash
cd Trabalho_Semestral
python wsgi.py
```

2. Inicie o servidor frontend:

```bash
cd Trabalho_Semestral
npm run serve
```

3. Abra seu navegador e acesse [http://localhost:8080](http://localhost:8080) (ou a porta especificada pelo seu servidor frontend) para ver a aplicação em execução.

## Contribuindo

Pull requests são bem-vindos. Para grandes alterações, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
