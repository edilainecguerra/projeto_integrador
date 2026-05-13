# Projeto Integrador - StudyFlow

Este projeto é uma aplicação Django.

## Pré-requisitos
- Python 3.8+
- pip


## Instalação

1. Clone o repositório e acesse a pasta do projeto.
2. (Opcional, mas recomendado) Crie e ative um ambiente virtual:

    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate    # Windows

3. Instale as dependências:

    pip install -r requirements.txt

4. Execute as migrações do banco de dados:

    python manage.py migrate

5. Inicie o servidor de desenvolvimento:

    python manage.py runserver

6. Acesse a aplicação em [http://localhost:8000](http://localhost:8000)

## Observações
- O banco de dados padrão é SQLite (db.sqlite3).
- Para criar um superusuário, execute:

    python manage.py createsuperuser

- O arquivo `.gitignore` já está configurado para ignorar arquivos de ambiente virtual, banco de dados e outros arquivos temporários.
