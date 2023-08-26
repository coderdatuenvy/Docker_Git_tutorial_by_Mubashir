FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install -y curl python3.11 python3.11-dev python3.11-distutils
RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py --force-reinstall && \
    rm get-pip.py
RUN pip3 install -U selenium 

RUN apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 ca-certificates
RUN apt-get install -y gnupg
RUN apt-get install -y wget xvfb unzip

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update -y
RUN apt-get install -y google-chrome-stable

RUN apt-get update -y



WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 8000

ENTRYPOINT  ["python3"]

CMD ["app.py"]