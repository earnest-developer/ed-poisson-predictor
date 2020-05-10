FROM python:3.7
COPY . /app
WORKDIR /app
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install -r requirements.txt
EXPOSE 50051
CMD python3 ./server.py