# PODCLASS

Um projeto para tentar classificar podcasts baseados nos gostos do usuário.

A aplicação é uma REST api para acessar os dados de podcasts através do feed rss.

As suas principais rotas e métodos estão no arquivo `main.py`.

`database.py` eh responsável por conectar com um banco sqlite para persistir as principais informações dos podcasts.

`rssfeed.py` fica responsável por se comunicar com a biblioteca que vai buscar os dados pelo link rss.

## Instalando

A aplicação usa um ambiente virtual python e cria uma pasta venv onde vamos instalar nossas bibliotecas. As dependências se encontram no arquivo `requirements.txt`.

Segue os camndos bash para ter seu ambiente pronto para uso.
```bash
# Prepare o ambiente
python3 -m venv venv 

# Ative o ambiente virutal
# No Windows
venv\Scripts\activate.bat
# No Unix
source venv/bin/activate

# Depois instale as dependencias
pip install -r requirements.txt
```

## Utilizando

Agora voce esta pronto para comecar a rodar o app.
Vamos adicionar a variável de ambiente que o Flask precisa para rodar o app e apenas pedir para o flask executar.
```bash
# No linux
export FLASK_APP=main
flask run
```

Pronto! Nossa aplicação esta pronta para ser utilizada!