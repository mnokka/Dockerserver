FROM python:2.7
RUN  pip install --verbose   Flask==0.12.1 uwsgi==2.0.8 logging 

WORKDIR /app
COPY app /app
RUN mkdir -p tmp

CMD ["python","/app/server.py"]