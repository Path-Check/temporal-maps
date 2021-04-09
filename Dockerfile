FROM ubuntu:18.04
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install build-essential
RUN apt-get -y install python3.8
RUN apt-get -y install python3-pip

COPY . app

WORKDIR app

RUN python3.8 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
#RUN python3.8 -m pip install -r requirements.txt

ENTRYPOINT ["python3.8","main.py"]
