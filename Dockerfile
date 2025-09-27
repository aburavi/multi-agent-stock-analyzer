FROM python:3.11-slim

WORKDIR /app

# Install system deps for pdfkit
RUN apt-get update && \
    apt-get install -y netcat-openbsd \
    wget \
    ca-certificates \
    fontconfig \
    libfreetype6 \
    libjpeg62-turbo \
    libpng16-16 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    xfonts-75dpi \
    xfonts-base \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_arm64.deb && \
    dpkg -i wkhtmltox_0.12.6.1-3.bookworm_arm64.deb && \
    apt-get install -f -y && \
    rm wkhtmltox_0.12.6.1-3.bookworm_arm64.deb

# Verify installation
RUN wkhtmltopdf --version

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy folder app
COPY ./app /app

COPY ./env.sample /.env

EXPOSE 8080

CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
