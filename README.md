# TODO-APP

## Descrição do Projeto
O **TODO-APP** é uma aplicação simples de gerenciamento de tarefas, desenvolvida utilizando Flask como framework para a criação de uma API RESTful, com persistência de dados em um banco de dados Oracle. O projeto foi containerizado utilizando Docker e Docker Compose para simplificar a implantação e o gerenciamento dos serviços.

## Objetivos
- Implementar uma API para gerenciar tarefas com operações CRUD (Create, Read, Update, Delete).
- Utilizar persistência de dados com OracleDB.
- Garantir a facilidade de implantação e escalabilidade com Docker e Docker Compose.

## Estrutura do Projeto
'''
TODO-APP/
├── api/
│   ├── app.py                # Código principal da API
│   └── requirements.txt      # Dependências do projeto
├── docker-compose.yml        # Configuração de serviços Docker
├── Dockerfile                # Configuração do container da aplicação
└── README.md                 # Este arquivo README
'''

## Pré-requisitos
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Configuração e Execução

1. **Clone o repositório:**
   git clone <link-do-repositorio>
   cd TODO-APP

2. **Configuração do Docker Compose:** Certifique-se de que o arquivo docker-compose.yml está configurado corretamente, incluindo o endereço do banco de dados Oracle.

3. **Inicie a aplicação com Docker Compose:**
   docker-compose up -d


Esse comando irá construir as imagens necessárias e iniciar os containers em background. A API estará disponível em http://localhost:5000.

4. **Testando a API:**
- Criar uma nova tarefa:
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Minha Tarefa", "description": "Descrição da tarefa"}'

- Listar todas as tarefas:
curl http://localhost:5000/tasks

- Atualizar uma tarefa existente:
curl -X PUT http://localhost:5000/tasks/1 -H "Content-Type: application/json" -d '{"title": "Novo Título", "description": "Nova descrição"}'

- Deletar uma tarefa:
curl -X DELETE http://localhost:5000/tasks/1

## Arquitetura do Projeto
A aplicação utiliza uma arquitetura de microserviços, com os seguintes componentes:

- API (Flask): Responsável pelo gerenciamento das tarefas com operações CRUD.
- Banco de Dados Oracle: Usado para armazenar os dados das tarefas de forma persistente.
- Docker e Docker Compose: Para orquestrar e gerenciar os containers da aplicação e do banco de dados.

## Notas Técnicas
- O arquivo Dockerfile foi configurado com uma imagem Python Slim para melhorar a eficiência e reduzir o tamanho do container.
- Docker Compose está configurado para mapear a porta 5000 do container para a porta 5000 do host.
- As variáveis de ambiente são definidas no docker-compose.yml para facilitar a configuração do banco de dados.
