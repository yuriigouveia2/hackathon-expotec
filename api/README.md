# Instruções para rodar API

## Criar ambiente de desenvolvimento utilizando ANACONDA
    conda create --name nomedoambiente python=3 

## Ativar ambiente de desenvolvimento 
    source activate nomedoambiente

## Instalar dependências necessárias
    pip install flask
    pip install flask-httpauth
    pip install Flask-PyMongo

## Iniciar o MongoDB
    sudo service mongod start

## Rodar aplicação
    python run.py