FROM python:3.10.12-alpine

WORKDIR /data

COPY . /data

RUN pip install -r requirements.txt

EXPOSE 6969

CMD python3 main.py
