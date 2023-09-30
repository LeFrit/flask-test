FROM python:3.9-slim

RUN pip install flask gunicorn

COPY src/ app/
WORKDIR /app

EXPOSE 8080

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app