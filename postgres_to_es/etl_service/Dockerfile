FROM python:3.10-alpine3.16

WORKDIR /etl_service

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

ADD entrypoint.sh movies.json /

RUN chmod +x '/entrypoint.sh'

RUN apk add --update netcat-openbsd \
     && apk --no-cache add curl

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt

COPY ./entrypoint.sh .entrypoint.sh 
COPY ./state.json .state.json
COPY ./movies.json .movies.json

COPY . .

ENTRYPOINT [ "sh", "./entrypoint.sh" ]
