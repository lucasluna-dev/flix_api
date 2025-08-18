Flix API

API para gerenciamento de filmes, atores, gêneros e avaliações.
Este projeto foi desenvolvido em Python com Django REST Framework, seguindo boas práticas de arquitetura e organização de código. O objetivo é fornecer uma base sólida para aplicações que necessitam de um backend robusto para operações de CRUD e consumo via REST.

Sumário

Tecnologias Utilizadas

Arquitetura do Projeto

Instalação

Configuração do Ambiente

Execução do Servidor

Endpoints Principais

Próximos Passos

Contribuição

Licença

Tecnologias Utilizadas

Python 3.12+

Django 5+

Django REST Framework

SQLite (banco padrão, mas facilmente adaptável para PostgreSQL/MySQL)

Virtualenv para gerenciamento de dependências

Arquitetura do Projeto

A estrutura do projeto segue a separação por domínios, cada módulo representando uma parte da aplicação:

flix_api/
│
├── actors/        # Funcionalidades relacionadas a atores
├── genres/        # Gerenciamento de gêneros
├── movies/        # Cadastro e listagem de filmes
├── reviews/       # Avaliações e notas
├── app/           # Configurações principais da aplicação
│
├── manage.py      # Utilitário de gerenciamento Django
└── requirements.txt

Instalação

Clone o repositório:

git clone https://github.com/lucasluna-dev/flix_api.git
cd flix_api


Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Instale as dependências:

pip install -r requirements.txt

Configuração do Ambiente

Antes de executar o projeto, configure o banco de dados e aplique as migrações:

python manage.py migrate


Opcional: crie um superusuário para acessar o painel administrativo:

python manage.py createsuperuser

Execução do Servidor

Inicie o servidor local:

python manage.py runserver


A aplicação ficará disponível em:

http://127.0.0.1:8000/

Endpoints Principais
Recurso	Método	Endpoint	Descrição
Filmes	GET	/movies/	Lista todos os filmes
Filmes	POST	/movies/	Cria um novo filme
Gêneros	GET	/genres/	Lista todos os gêneros
Atores	GET	/actors/	Lista todos os atores
Avaliações	GET	/reviews/	Lista todas as avaliações

(Os endpoints podem variar conforme a implementação. Consulte os arquivos de views/serializers para detalhes.)

Próximos Passos

Adicionar autenticação JWT para segurança da API

Criar documentação interativa com Swagger ou Redoc

Implementar testes automatizados (unitários e integração)

Melhorar o versionamento da API (ex: /api/v1/)