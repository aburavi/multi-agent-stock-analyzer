FROM python:3.11-slim

WORKDIR /app

# Install system deps for pdfkit
RUN apt-get update && apt-get install -y netcat-openbsd \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy folder app
COPY ./app /app

COPY ./env.sample /.env

EXPOSE 8080

CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
