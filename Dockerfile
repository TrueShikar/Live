FROM nikolaik/python-nodejs:python3.9-nodejs18
RUN apt-get update && apt-get upgrade -y
RUN apt install ffmpeg -y
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD python3 main.py
