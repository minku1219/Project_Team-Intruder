FROM ubuntu
# MAINTAINER minku1219@gmail.com
RUN apt update -y
RUN apt install apache2 -y && apt clean
WORKDIR /var/www/html/
ADD index.html /var/www/html/index.html
EXPOSE 80
#CMD apache2ctl -D FOREGROUND
# CMD apache2 -k start
ENTRYPOINT apache2ctl -D FOREGROUND

