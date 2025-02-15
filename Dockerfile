# Usa a imagem oficial do Python
FROM python:3.12

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Instala o Poppler para suportar pdf2image
RUN apt-get update && apt-get install -y poppler-utils

# Define o comando padrão para rodar o script
CMD ["python", "converter.py"]
