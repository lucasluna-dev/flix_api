<!-- README rendered as HTML for GitHub (works inside README.md). No emojis; clean, professional formatting. -->
<div id="readme" style="font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #111;">
  <h1 style="margin-bottom: 0.2rem;">Flix API</h1>
  <p style="margin-top: 0; max-width: 900px;">
    API para gerenciamento de filmes, atores, gêneros e avaliações. Este projeto foi desenvolvido em Python com Django REST Framework, seguindo boas práticas de arquitetura e organização de código.
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
      <li><a href="#endpoints">Endpoints Principais</a></li>
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

  <!-- Execucao -->
  <h2 id="execucao">Execução do Servidor</h2>
  <pre style="background:#0b1021; color:#e6e6e6; padding:14px; border-radius:8px; overflow:auto;"><code class="language-bash">python manage.py runserver</code></pre>
  <p>Aplicação disponível em <code>http://127.0.0.1:8000/</code>.</p>

  <!-- Endpoints -->
  <h2 id="endpoints">Endpoints Principais</h2>
  <p>Rotas típicas para os recursos. Ajuste conforme sua implementação atual.</p>
  <div style="overflow-x:auto;">
    <table style="border-collapse: collapse; width: 100%; min-width: 520px;">
      <thead>
        <tr>
          <th style="text-align:left; border-bottom:1px solid #e5e7eb; padding:8px;">Recurso</th>
          <th style="text-align:left; border-bottom:1px solid #e5e7eb; padding:8px;">Método</th>
          <th style="text-align:left; border-bottom:1px solid #e5e7eb; padding:8px;">Endpoint</th>
          <th style="text-align:left; border-bottom:1px solid #e5e7eb; padding:8px;">Descrição</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Filmes</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">GET</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;"><code>/movies/</code></td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Lista todos os filmes</td>
        </tr>
        <tr>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Filmes</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">POST</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;"><code>/movies/</code></td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Cria um novo filme</td>
        </tr>
        <tr>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Gêneros</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">GET</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;"><code>/genres/</code></td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Lista todos os gêneros</td>
        </tr>
        <tr>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Atores</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">GET</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;"><code>/actors/</code></td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Lista todos os atores</td>
        </tr>
        <tr>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Avaliações</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">GET</td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;"><code>/reviews/</code></td>
          <td style="border-bottom:1px solid #f0f0f0; padding:8px;">Lista todas as avaliações</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p style="font-size: 0.95em; color:#444; margin-top: 0.75rem;">Observação: a nomenclatura e a estrutura dos endpoints podem variar de acordo com as <em>views</em> e <em>serializers</em> configurados no projeto.</p>

  <!-- Roadmap -->
  <h2 id="roadmap">Próximos Passos</h2>
  <ul>
    <li>Adicionar autenticação JWT para segurança da API.</li>
    <li>Documentação interativa com Swagger ou Redoc.</li>
    <li>Testes automatizados (unitários e integração).</li>
    <li>Versionamento da API (ex.: <code>/api/v1/</code>).</li>
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
  </p>
</div>
