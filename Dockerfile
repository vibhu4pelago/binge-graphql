FROM python:3.11-alpine

COPY requirements.txt /binge-graphql/requirements.txt

WORKDIR /binge-graphql

RUN pip install -r requirements.txt

COPY ./src /binge-graphql/src

EXPOSE 5000

CMD ["python", "src/app.py"]
