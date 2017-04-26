FROM python:3.5
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD . /code/
ADD requirements.txt /code/
ADD requirements-deploy.txt /code/
RUN pip install -r requirements.txt
RUN pip install -r requirements-deploy.txt
ADD signbank/settings/docker.py /code/signbank/settings/live.py
RUN apt-get install -y libav-tools
