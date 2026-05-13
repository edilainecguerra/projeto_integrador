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

## Internationalization (i18n) and Translations

This project supports multiple languages using Django's i18n system. To add or edit translations:

1. Mark all user-facing text in your templates with `{% trans "Text" %}` and in Python code with `gettext_lazy("Text")` or `_("Text")`.
2. Run the following command to extract translation strings and create the translation file for Brazilian Portuguese:

    python manage.py makemessages -l pt_BR

   This will create the file `locale/pt_BR/LC_MESSAGES/django.po`.

3. Open `django.po` and fill in the `msgstr` fields with the Portuguese translations for each `msgid`.

4. After editing and saving the `.po` file, compile the translations with:

    python manage.py compilemessages

Django will then use these translations automatically based on the user's language preference.