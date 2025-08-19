
FROM python:3.9


WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir "PyYAML==5.4.1" --only-binary :all: || true
RUN pip install --no-cache-dir -r/app/requirements.txt

COPY . /app
RUN rasa train
RUN pip install --no-cache-dir "pyyaml==5.4.1" --only-binary :all:
RUN chmod +x /app/start.sh






EXPOSE 8501 5005 5055


CMD ["bash","./start.sh"]
