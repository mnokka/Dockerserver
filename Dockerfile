FROM python:2.7

RUN pip install Flask==0.10.1
WORKDIR /app
COPY app /app

CMD ["python","server.py"]