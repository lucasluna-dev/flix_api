<!-- README rendered as HTML for GitHub (works inside README.md). No emojis; clean, professional formatting. -->
<div id="readme" style="font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #111;">
  <h1 style="margin-bottom: 0.2rem;">Flix API</h1>
  <p style="margin-top: 0; max-width: 900px;">
    API para gerenciamento de filmes, atores, gêneros e avaliações. Este projeto foi desenvolvido em Python com Django REST Framework, com autenticação JWT e controle de permissões por modelo.
  </p>

  <hr style="border: 0; border-top: 1px solid #e5e7eb; margin: 1.25rem 0;" />

  <!-- Sumário -->
  <nav aria-label="Sumário" style="margin: 1rem 0 1.5rem;">
    <strong>Sumário</strong>
    <ul style="margin: 0.25rem 0 0 1.2rem;">
      <li><a href="#tecnologias">Tecnologias Utilizadas</a></li>
      <li><a href="#arquitetura">Arquitetura do Projeto</a></li>
      <li><a href="#instalacao">Instalação</a></li>
      <li><a href="#configuracao">Configuração do Ambiente</a></li>
      <li><a href="#execucao">Execução do Servidor</a></li>
      <li><a href="#funcionalidades">Funcionalidades</a></li>
      <li><a href="#endpoints">Endpoints</a></li>
      <li><a href="#roadmap">Próximos Passos</a></li>
      <li><a href="#contribuicao">Contribuição</a></li>
      <li><a href="#licenca">Licença</a></li>
    </ul>
  </nav>

  <!-- Tecnologias -->
  <h2 id="tecnologias">Tecnologias Utilizadas</h2>
  <ul>
    <li>Python 3.12+</li>
    <li>Django 5.x</li>
    <li>Django REST Framework</li>
    <li>SQLite (padrão; adaptável para PostgreSQL/MySQL)</li>
    <li>Virtualenv para isolamento de dependências</li>
    <li>SimpleJWT (autenticação via tokens JWT)</li>
  </ul>

  <!-- Arquitetura -->
  <h2 id="arquitetura">Arquitetura do Projeto</h2>
  <p>A estrutura adota separação por domínio (features), facilitando manutenção e escalabilidade.</p>
  <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;">
<code>flix_api/
├── actors/        # Regras e endpoints de atores
├── genres/        # Regras e endpoints de gêneros
├── movies/        # Regras e endpoints de filmes
├── reviews/       # Regras e endpoints de avaliações
├── app/           # Configurações centrais do projeto
├── manage.py      # Utilitário de gerenciamento (Django)
└── requirements.txt
</code></pre>

  <!-- Funcionalidades -->
  <h2 id="funcionalidades">Funcionalidades</h2>
  <ul>
    <li>Autenticação JWT com rotas de login, refresh e verificação.</li>
    <li>Cadastro de usuários e endpoint de perfil do usuário autenticado.</li>
    <li>CRUD completo para Atores, Gêneros, Filmes e Avaliações.</li>
    <li>Política de autorização por permissões de modelo via <code>GlobalDefaultPermissionClass</code>.</li>
    <li>Endpoint de estatísticas de filmes (totais, médias de avaliações).</li>
    <li>Versionamento de rotas sob o prefixo <code>/api/v1/</code>.</li>
  </ul>

  <!-- Instalacao -->
  <h2 id="instalacao">Instalação</h2>
  <ol>
    <li>
      <p>Clone o repositório:</p>
      <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code class="language-bash">git clone https://github.com/lucasluna-dev/flix_api.git
cd flix_api</code></pre>
    </li>
    <li>
      <p>Crie e ative um ambiente virtual:</p>
      <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code class="language-bash">python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows</code></pre>
    </li>
    <li>
      <p>Instale as dependências:</p>
      <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code class="language-bash">pip install -r requirements.txt</code></pre>
    </li>
  </ol>

  <!-- Configuracao -->
  <h2 id="configuracao">Configuração do Ambiente</h2>
  <p>Aplicar migrações e, opcionalmente, criar um superusuário para acessar o admin.</p>
  <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code class="language-bash">python manage.py migrate
python manage.py createsuperuser  # opcional</code></pre>
  <p style="margin-top: 0.5rem;">Permissões padrão de leitura podem ser atribuídas executando o comando abaixo, que cria (ou atualiza) o grupo <code>default_viewer</code> com todas as permissões <code>view_*</code> para os apps de domínio:</p>
  <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code class="language-bash">python manage.py setup_default_permissions</code></pre>
  <p>Novos usuários cadastrados são adicionados automaticamente ao grupo <code>default_viewer</code> (se existir).</p>

  <!-- Execucao -->
  <h2 id="execucao">Execução do Servidor</h2>
  <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code class="language-bash">python manage.py runserver</code></pre>
  <p>Aplicação disponível em <code>http://127.0.0.1:8000/</code>.</p>

  <!-- Endpoints -->
  <h2 id="endpoints">Endpoints</h2>
  <p>Todos os endpoints abaixo estão sob o prefixo <code>/api/v1/</code> e exigem autenticação (JWT), exceto onde indicado.</p>

  <h3 style="margin-bottom: 0.4rem;">Autenticação</h3>
  <ul>
    <li><code>POST /api/v1/authentication/register/</code> — cadastro (acesso público).</li>
    <li><code>POST /api/v1/authentication/token/</code> — login, retorna <code>access</code> e <code>refresh</code>.</li>
    <li><code>POST /api/v1/authentication/token/refresh/</code> — renova <code>access</code>.</li>
    <li><code>POST /api/v1/authentication/token/verify/</code> — verifica token.</li>
    <li><code>GET /api/v1/authentication/me/</code> — dados do usuário autenticado.</li>
  </ul>

  <h3 style="margin-bottom: 0.4rem;">Filmes</h3>
  <ul>
    <li><code>GET/POST /api/v1/movies/</code> — lista/cria filmes.</li>
    <li><code>GET/PUT/PATCH/DELETE /api/v1/movies/&lt;pk&gt;/</code> — detalhe/atualiza/remove.</li>
    <li><code>GET /api/v1/movies/stats/</code> — estatísticas: total de filmes, total por gênero, total de reviews e média geral de estrelas.</li>
  </ul>

  <h3 style="margin-bottom: 0.4rem;">Gêneros</h3>
  <ul>
    <li><code>GET/POST /api/v1/genres/</code> — lista/cria gêneros.</li>
    <li><code>GET/PUT/PATCH/DELETE /api/v1/genres/&lt;pk&gt;/</code> — detalhe/atualiza/remove.</li>
  </ul>

  <h3 style="margin-bottom: 0.4rem;">Atores</h3>
  <ul>
    <li><code>GET/POST /api/v1/actors/</code> — lista/cria atores.</li>
    <li><code>GET/PUT/PATCH/DELETE /api/v1/actors/&lt;id&gt;/</code> — detalhe/atualiza/remove.</li>
  </ul>

  <h3 style="margin-bottom: 0.4rem;">Avaliações</h3>
  <ul>
    <li><code>GET/POST /api/v1/reviews/</code> — lista/cria avaliações.</li>
    <li><code>GET/PUT/PATCH/DELETE /api/v1/reviews/&lt;pk&gt;/</code> — detalhe/atualiza/remove.</li>
  </ul>

  <p style="font-size: 0.95em; color:#444; margin-top: 0.5rem;">
    Observações:
    <br />• O serializer de filmes expõe o campo somente leitura <code>rate</code> (média de estrelas das avaliações).
    <br />• Validações: <code>release_date</code> não pode ser anterior a 1990; <code>resume</code> com no máximo 100 caracteres.
  </p>

  <!-- Autenticacao -->
  <h2 id="auth">Autenticação e Cadastro</h2>
  <p>Autenticação via JWT (SimpleJWT) já configurada. Fluxos:</p>
  <ul>
    <li><code>POST /api/v1/authentication/register/</code> – cria usuário com <em>password</em> seguro. Campos: <code>username</code>, <code>email</code>, <code>password</code>, <code>password2</code>, <code>first_name</code>, <code>last_name</code>.</li>
    <li><code>POST /api/v1/authentication/token/</code> – login, retorna <code>access</code> e <code>refresh</code>.</li>
    <li><code>POST /api/v1/authentication/token/refresh/</code> – renova <code>access</code>.</li>
    <li><code>POST /api/v1/authentication/token/verify/</code> – verifica validade do token.</li>
    <li><code>GET /api/v1/authentication/me/</code> – dados do usuário autenticado.</li>
  </ul>
  <p style="margin-top: 0.5rem;">
    Política de autorização: todas as views de domínio usam <code>IsAuthenticated</code> + <code>GlobalDefaultPermissionClass</code>.
    O mapeamento de método → permissão de modelo é:
  </p>
  <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code>GET/HEAD/OPTIONS → view_*
POST              → add_*
PUT/PATCH         → change_*
DELETE            → delete_*</code></pre>
  <p>Conceda permissões via grupos no admin do Django ou use o comando de setup de permissões (ver Configuração do Ambiente).</p>

  <!-- Exemplos -->
  <h3 style="margin-top: 1rem;">Exemplos de uso (cURL)</h3>
  <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code class="language-bash"># 1) Cadastro
curl -X POST http://127.0.0.1:8000/api/v1/authentication/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com","password":"secret123","password2":"secret123"}'

# 2) Login (JWT)
curl -X POST http://127.0.0.1:8000/api/v1/authentication/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"secret123"}'
# → copie o valor de access

# 3) Listar filmes
curl http://127.0.0.1:8000/api/v1/movies/ -H "Authorization: Bearer &lt;ACCESS_TOKEN&gt;"

# 4) Estatísticas de filmes
curl http://127.0.0.1:8000/api/v1/movies/stats/ -H "Authorization: Bearer &lt;ACCESS_TOKEN&gt;"</code></pre>

  <!-- Scripts utilitarios -->
  <h3 style="margin-top: 1rem;">Scripts Utilitários</h3>
  <p>Há um smoke test para o endpoint de estatísticas em <code>scripts/smoke_stats.py</code> que cria dados mínimos e imprime o JSON de resultado:</p>
  <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code class="language-bash">python manage.py shell -c "import scripts.smoke_stats as s; s.run()"</code></pre>

  <!-- Roadmap -->
  <h2 id="roadmap">Próximos Passos</h2>
  <ul>
    <li>Documentação interativa com Swagger ou Redoc.</li>
    <li>Testes automatizados (unitários e integração).</li>
    <li>Paginação, filtros e ordenação nos endpoints de lista.</li>
    <li>Polir validações e mensagens de erro.</li>
  </ul>

  <!-- Notas de Producao -->
  <h3 style="margin-top: 0.75rem;">Notas para Produção</h3>
  <ul>
    <li>Definir <code>DEBUG=False</code> e <code>ALLOWED_HOSTS</code> adequados.</li>
    <li>Configurar banco de dados gerenciado (ex.: PostgreSQL) e variáveis de ambiente.</li>
    <li>Avaliar tempos de expiração do JWT (atualmente <code>ACCESS_TOKEN_LIFETIME=365 dias</code>, <code>REFRESH=5 anos</code> em <code>app/settings.py</code>).</li>
    <li>Executar atrás de ASGI (Uvicorn/Daphne) e proxy reverso (Nginx).</li>
  </ul>

  <!-- Contribuicao -->
  <h2 id="contribuicao">Contribuição</h2>
  <ol>
    <li>Faça um fork do repositório.</li>
    <li>Crie uma branch para sua alteração: <code>git checkout -b minha-feature</code>.</li>
    <li>Commit das mudanças: <code>git commit -m "feat: descreva sua mudança"</code>.</li>
    <li>Envie para a origem: <code>git push origin minha-feature</code>.</li>
    <li>Abra um Pull Request com a descrição do que foi feito.</li>
  </ol>

  <!-- Licenca -->
  <h2 id="licenca">Licença</h2>
  <p>Distribuído sob a licença MIT. Consulte o arquivo <code>LICENSE</code> para mais informações.</p>

  <hr style="border: 0; border-top: 1px solid #e5e7eb; margin: 1.75rem 0 0.75rem;" />
  <p style="font-size: 0.92em; color:#555;">Dicas:
    <br />• Para ambientes de produção, considere <strong>PostgreSQL</strong> como banco de dados e um servidor ASGI (Daphne/Uvicorn) por trás de um <em>reverse proxy</em>.
    <br />• Configure variáveis de ambiente para credenciais e chaves, evitando expô-las no controle de versão.
    <br />• Admin do Django disponível em <code>/admin/</code> para gerenciar permissões e dados.
  </p>
</div>
