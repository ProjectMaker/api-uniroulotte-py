FROM python:3.7-alpine

COPY ./app /app

WORKDIR /app



ENTRYPOINT [ "python" ]

CMD [ "app.py" ]