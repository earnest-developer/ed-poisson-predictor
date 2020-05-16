FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
EXPOSE 50051
CMD python3 ./server.py