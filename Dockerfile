FROM python:3.8-slim-bullseye

RUN apt update; apt-get install -y libgdal-dev g++ --no-install-recommends && \
    apt-get clean -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]