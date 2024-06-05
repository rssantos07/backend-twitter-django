## Twitter Clone

<p align="center">Este projeto é um backend para uma rede social simples, inspirado no Twitter, construído com Django e Django REST Framework (DRF). Ele fornece endpoints para autenticação de usuários, gerenciamento de perfis, criação e visualização de posts com imagens, e um endpoint de teste.</p>


# Funcionalidades
- Autenticação:
- Registro de novos usuários (/api/register/).
- Login com obtenção de token de acesso (/api/token/).
- Atualização de token de acesso (/api/token/refresh/).
- Usuários:
- Visualização de informações do perfil do usuário logado (/api/user/).
- Visualização de informações de um usuário específico (/api/user/<id>/).

# Posts:
- Criação de posts com texto e imagem (opcional) (/api/posts/).
- Listagem de todos os posts (/api/posts/).
- Exclusão de posts (/api/posts/<id>/).
- Endpoint de Teste:
- Endpoint para testar a autenticação e o envio de dados (/api/test/).
- Modelos

# User:
- Estende o modelo AbstractUser do Django.
- Campos: username (CharField), email (EmailField, unique).
- email é usado como nome de usuário para login.

# Profile:
- Relacionamento OneToOne com User.
- Campos: full_name (CharField), bio (CharField), image (ImageField), verified (BooleanField).

# Post:
- Relacionamento ForeignKey com User.
- Campos: mensagem (TextField), imagem (ImageField, opcional), created_at (DateTimeField).

# Serializers:
- RegisterSerializer: Serializa os dados para o registro de novos usuários.
- MyTokenObtainPairSerializer: Serializa os dados para a obtenção de tokens de acesso e atualização (login).
- UserSerializer: Serializa os dados do usuário, incluindo informações do perfil.
- PostSerializer: Serializa os dados dos posts.

# Views/ViewSets
- MyTokenObtainPairView: View para obter o par de tokens (login).
- RegisterView: View para registro de novos usuários.
- UserViewSet: ViewSet para gerenciar usuários e seus perfis.
- PostViewSet: ViewSet para gerenciar posts.

# Endpoints
- GET /api/: Retorna uma lista com todos os endpoints da API.
- POST /api/register/: Registra um novo usuário.
- POST /api/token/: Obtém um token de acesso para um usuário existente.
- POST /api/token/refresh/: Atualiza um token de acesso expirado.
- GET /api/user/: Retorna informações do usuário logado (lista com um único item).
- GET /api/user/<id>/: Retorna informações de um usuário específico.
- POST /api/posts/: Cria um novo post.
- GET /api/posts/: Retorna todos os posts.
- DELETE /api/posts/<id>/: Exclui um post.
- GET/POST /api/test/: Endpoint de teste para verificar a autenticação.

Como usar
1. Clone o repositório:
git clone https://github.com/rssantos07/backend-twitter-django.git

2. Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Rode as migrações
python manage.py migrate

5. Execute o servidor de desenvolvimento:
python manage.py runserver

6. Acesse a API: A API estará disponível em http://127.0.0.1:8000/api/.

