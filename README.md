# Django Raster Uploader

Este é um projeto desenvolvido em Django para upload de arquivos raster para o Geoserver via interface web.

## Rodando o projeto localmente

Clonar o projeto:
```bash
git clone https://git.pti.org.br/it.dt/nit/territorio/provas_de_conceito/django-raster-uploader.git
```

Criar venv python:
```bash
python3 -m venv .venv
```

Instalar requirements:
```bash
pip install -r requirements.txt
```

Aplicar as migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Rodar o servidor de testes:
```bash
python manage.py runserver
```

O projeto estará disponível em **127.0.0.1:8000**.

Para acessar o painel admin, crie um super usuário:
```bash
python manage.py createsuperuser
```
E vá até **127.0.0.1:8000/admin**.

## Utilizando o Docker

**Importante:** Antes de subir a aplicação, é necessário apontar para um Geoserver acessível no arquivo .env

Na pasta do projeto, utilize os seguintes comandos
```bash
docker build --tag django-raster-uploader .
docker run --publish 8000:8000 django-raster-uploader
```
