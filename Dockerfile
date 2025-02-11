FROM python:3.9-slim

RUN mkdir /app

COPY ./app /app
COPY requirements.txt /app/requirements.txt 

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "-m", "uvicorn", "main:app"]
