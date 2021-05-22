FROM python:3.7
WORKDIR /usr/src/app
 
COPY requirements.txt ./
RUN pip install  flask gunicorn gevent 
 
COPY . .
 
CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
