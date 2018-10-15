FROM python:3.7-alpine

COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock

WORKDIR /code

RUN apk add --no-cache build-base python-dev py-pip jpeg-dev zlib-dev yarn
ENV LIBRARY_PATH=/lib:/usr/lib

RUN pip install pipenv==2018.6.25 pip==18.0 && \
    pipenv install --system --deploy --ignore-pipfile

COPY . /code

RUN yarn install

EXPOSE 8000

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "senne.wsgi"]