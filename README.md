# Projeto Final Backend
API desenvolvida como projeto final para formação no Projeto Desenvolve, utilizando o **FastAPI**, **Alembic** e **SQLAlchemy**. O sistema permite a gestão de alunos, cursos e o controle de matrículas.

### Como rodar o projeto:


1. Clone o repositório: *git clone [https://github.com/leirioli/projetofinalbackend.git](https://github.com/leirioli/projetofinalbackend.git)
   cd projetofinalbackend*
2. Crie um ambiente virtual:
   *python -m venv venv*
   - **Ativar no Windows**: *.\venv\Scripts\activate*
   - **Ativar no Linux/Mac**: *source venv/bin/activate*
3. Instale as dependências: *pip install -r requirements.txt*
4. Por fim, inicie o servidor: *uvicorn main:app --reload*

### Como configurar o banco de dados:


O projeto utiliza o SQLite, com as tabelas sendo gerenciados pelo Alembic, para a criação do banco de dados e das tabelas, execute:
+ *alembic upgrade head*


Isso criará o arquivo **database.db** com as tabelas.


### Endpoints:


**Alunos**
+ POST /alunos/ - Cadastra um aluno
+ GET /alunos/ - Lista todos os alunos
+ GET /alunos/{aluno_id} - Busca aluno por id
+ PUT /alunos/{aluno_id} - Atualiza os dados do aluno
+ DELETE /alunos/{aluno_id} - Remove um aluno do sistema


**Cursos**
+ GET /cursos/ - Lista todos os cursos
+ POST /cursos/ - Cadastra um curso
+ GET /cursos/{curso_id} - Busca um curso por id
+ PUT /cursos/{curso_id} - Atualiza os dados do curso
+ DELETE /cursos/{curso_id} - Remove um curso do sistema


**Matriculas**
+ POST /matriculas/ - Matricula um aluno em um curso (limite de 5 matrículas ativas)
+ GET /matriculas/aluno/{aluno_id} - Lista todos os cursos de um aluno específico
+ GET /matriculas/curso/{curso_id} - Lista todos os alunos de um curso específico
+ PATCH /matriculas/{matricula_id}/cancelar - Altera o status da matrícula para "cancelada"
+ PATCH /matriculas/{matricula_id}/concluir - Altera o status da matrícula para "concluida"


## Deploy


Plataforma: Render<br>
Link: https://projetofinalbackend-jhnv.onrender.com/docs<br>
O Render utiliza a variável padrão PORT para expor a aplicação.
