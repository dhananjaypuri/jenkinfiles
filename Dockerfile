FROM python:3.9-slim

WORKDIR /app

COPY . /app/

pip install -r requirements.txt

CMD python app.py