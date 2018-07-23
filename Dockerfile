FROM python:3.6-alpine

COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock

WORKDIR /code

RUN apk add --no-cache build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

RUN pip install -U pip && \
    pip install pipenv && \
    pipenv install

COPY . /code

EXPOSE 8888

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8888"]