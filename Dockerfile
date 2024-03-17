FROM ubuntu:22.04
COPY . .
RUN apt-get update -y 
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
RUN python3 init_db.py
CMD [ "python3", "main.py" ]
