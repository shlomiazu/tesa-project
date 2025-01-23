FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y redis-server

WORKDIR /app

COPY ../../TASE/app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["redis-server"]