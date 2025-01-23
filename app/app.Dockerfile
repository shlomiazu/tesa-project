FROM python:3.9-slim-buster

WORKDIR /app

COPY ../../TASE/app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ../app .

CMD ["python", "app.py"]