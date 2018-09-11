FROM python:3-alpine
LABEL maintainer "Bearnard Hibbins <bearnard@gmail.com>"

ENV TESTAPP_VERSION 0.2.0

COPY server.py /
COPY requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "-u", "server.py" ]
