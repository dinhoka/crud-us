
#CRUD de Usuário com Flask e SQLite
Este é um projeto de exemplo de um aplicativo CRUD (Create, Read, Update, Delete) de usuário desenvolvido em Python com o framework Flask e utilizando um banco de dados SQLite. O aplicativo permite criar, listar, atualizar e excluir usuários.

Configuração do Ambiente
Certifique-se de ter o Python instalado em seu sistema. Você pode fazer o download em python.org.

Clone este repositório para o seu ambiente de desenvolvimento:


git clone https://github.com/seu-usuario/crud-usuario-flask-sqlite.git
Navegue até o diretório do projeto:

bash
Copy code
cd crud-usuario-flask-sqlite
Crie um ambiente virtual para isolar as dependências do projeto:

bash
Copy code
python -m venv venv
Ative o ambiente virtual:

No Windows:
bash
Copy code
venv\Scripts\activate
No macOS e Linux:
bash
Copy code
source venv/bin/activate
Instale as dependências do projeto:

bash
Copy code
pip install -r requirements.txt
Executando o Aplicativo
Certifique-se de que você está no ambiente virtual ativado e no diretório do projeto.

Execute o aplicativo Flask:


python app.py
O aplicativo será executado em http://127.0.0.1:5000/ no seu navegador. Você verá a página inicial com links para cada funcionalidade do CRUD.

Uso do Aplicativo
Clique nos links na página inicial para cadastrar, listar, atualizar e excluir usuários.
Preencha os formulários para cada operação (Cadastro, Atualização) e siga as instruções na interface do aplicativo.
Os dados dos usuários serão armazenados no banco de dados SQLite (banco.db) no diretório do projeto.
Estrutura do Projeto
app.py: O arquivo principal do aplicativo Flask.
banco.db: O arquivo do banco de dados SQLite.
templates/: Contém os modelos HTML para as páginas do aplicativo.
static/: Contém arquivos estáticos, como folhas de estilo CSS, se necessário.
Contribuição
Sinta-se à vontade para contribuir para este projeto ou relatar problemas encontrados. Basta criar uma "issue" no repositório ou enviar um "pull request" com suas alterações.
