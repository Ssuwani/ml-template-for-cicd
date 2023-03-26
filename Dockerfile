FROM python:3.10

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /src
WORKDIR /src

ENTRYPOINT ["python", "main.py"]
CMD [ "" ]