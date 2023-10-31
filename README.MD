# Sync and Async testing

Testando chamadas síncronas e assíncronas

## Deploy

### 1. Install virtual env

1. instalar venv
```shell
python -m venv venv
```
2. ativar venv
```shell
source venv/bin/activate 
```

### 2. Instalar dependências
```
pip install -r requirements.txt
```
### 3. Subir servidor uvicorn

```shell
python -m uvicorn --reload asyncviews.asgi:application
```