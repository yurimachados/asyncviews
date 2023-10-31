# Sync and Async testing

Este repositório é dedicado a explorar e demonstrar as diferenças entre abordagens síncronas e assíncronas na programação de APIs. Como desenvolvedor no Brasil, estou comprometido em fornecer insights valiosos e exemplos práticos para aprimorar suas habilidades no desenvolvimento de APIs tanto no ambiente de programação síncrona quanto assíncrona.

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
