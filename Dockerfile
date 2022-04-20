FROM ubuntu:20.04
ENV DEBIAN_FRONTEND='noninteractive'
COPY app.py /var/www/app/app.py
COPY tests /var/www/app/tests
COPY requirements.txt /var/www/app/requirements.txt
RUN apt-get update && \
    mkdir -vp /var/www/app && \
    apt-get install -y locales pkg-config curl python3-pip && \
    locale-gen "en_US.UTF-8" && \
    dpkg-reconfigure locales && \
    python3 -m pip install -r /var/www/app/requirements.txt
CMD ["/usr/local/bin/uwsgi", "--http", ":8080", "--wsgi-file", "/var/www/app/app.py", "--callable", "app"]
