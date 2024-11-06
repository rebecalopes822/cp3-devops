# use uma imagem base com python
FROM python:3.9-slim

# para definir o diretório de trabalho
WORKDIR /app

# copie o arquivo de requisitos e instale as dependências
COPY api/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copie o código da API para o container
COPY api/ ./

# para rodar o Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
