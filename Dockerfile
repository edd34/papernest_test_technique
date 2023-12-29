FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt
RUN pip3 install uvicorn
COPY . /code/