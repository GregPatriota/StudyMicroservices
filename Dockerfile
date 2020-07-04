FROM python:3.7-alpine as base

WORKDIR /app

COPY . .

RUN apk update && \
    apk add alpine-sdk libffi-dev && \
    pip install -r requirements.txt

FROM base as main

CMD ["python", "main/root.py"]