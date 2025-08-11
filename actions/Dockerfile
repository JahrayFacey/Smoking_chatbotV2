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

EXPOSE 5055
CMD ["run", "actions", "--port", "5055"]