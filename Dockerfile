FROM python:3.10.12-alpine

WORKDIR /docker-container-webui

COPY . /docker-container-webui

RUN pip install -r requirements.txt

EXPOSE 6969

CMD python3 main.py
