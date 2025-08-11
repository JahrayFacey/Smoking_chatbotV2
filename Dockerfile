
FROM python:3.9


WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    git \
    curl \
    libffi-dev \
    libssl-dev \
    libgomp1 \
    cython3 \
    && rm -rf /var/lib/apt/lists/*

COPY . /app


RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir "pyyaml==5.4.1" --only-binary :all:
RUN pip install --no-cache-dir -r requirements.txt



EXPOSE 8501 5005


CMD rasa run --enable-api --cors "*" --port 5005 --model models & streamlit run home.py --server.port=8501 --server.address=0.0.0.0
