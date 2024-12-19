FROM python:3.10

RUN apt-get update && apt-get install -y \
    build-essential \
    libboost-all-dev \
    libprotobuf-dev \
    libsnappy-dev \
    liblz4-dev \
    libzstd-dev \
    libjemalloc-dev \
    cmake \
    clang \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY ./requirements_docker.txt ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --prefer-binary --no-cache-dir -r requirements_docker.txt

COPY ./ ./

CMD ["streamlit", "run", "monitorzeiten.py", "--server.port", "8501"]
