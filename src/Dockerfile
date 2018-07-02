FROM python:3.6.1-alpine
MAINTAINER vgs

RUN apk --update --no-cache add openssl ca-certificates curl
ADD certs/* /usr/local/share/ca-certificates/
RUN update-ca-certificates

ADD healthcheck /src
WORKDIR /src
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "healthcheck.py"]