# fastapi.tiangolo.com-tutorial-body

- Request Body

- Reference: https://fastapi.tiangolo.com/tutorial/body/

## pyenv

```sh
pyenv install 3.11
pyenv global 3.11
```

## poetry

- Install poetry 1.8.2 via pipx

```sh
pipx install --suffix=@1.8.2 poetry==1.8.2
pipx ensurepath
source ~/.bashrc
poetry@1.8.2 --version  # Poetry (version 1.8.2)
```

- Activating the environment

```sh
poetry@1.8.2 env use python3.11
poetry@1.8.2 run python --version   # Python 3.11.10
```

## Install dependencies

```sh
poetry@1.8.2 install
```

## FastAPI

```sh
poetry@1.8.2 run fastapi dev tutorial_body/main.py
```

## cURL

### GET /hello

```sh
curl --location 'localhost:8000/hello'
```

### POST /items

```sh
curl -X 'POST' \
    'http://localhost:8000/items' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "NAME",
        "price": 0,
        "description": "DESCRIPTION",
        "tax": 0
    }'
```

```sh
curl -X 'POST' \
    'http://localhost:8000/items' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "NAME",
        "price": 0
    }'
```

```sh
curl -X 'POST' \
    'http://localhost:8000/items' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "NAME"
    }'
```
