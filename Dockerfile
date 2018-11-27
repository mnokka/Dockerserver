FROM python:2.7
RUN  pip install --verbose   Flask==0.12.1 uwsgi==2.0.17.1 logging 

WORKDIR /app
COPY app /app
RUN mkdir -p tmp


CMD ["uwsgi","--http","0.0.0.0:9090","--wsgi-file","/app/server.py","--callable","app","--stats","0.0.0.0:9191"]
