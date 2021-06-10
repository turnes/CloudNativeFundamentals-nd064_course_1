FROM python:3.9-rc-slim as dev

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV=development

CMD [ "python", "app.py" ]

FROM python:3.9-rc-slim as prod

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]