FROM python:3.9-slim

RUN mkdir /app

COPY ./app /app

WORKDIR /app

CMD ["uvicorn", "main:app"]