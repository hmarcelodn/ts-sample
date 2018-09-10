FROM python:3.6

RUN apt-get update && apt-get install -y libgeos-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD ["uwsgi", "uwsgi.ini"]