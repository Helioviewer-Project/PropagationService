FROM python:3

RUN echo "deb http://ftp.belnet.be/debian/ testing main" >> /etc/apt/sources.list

#2.12.14 spyne has a bug solved on github
ADD ./external/spyne /python/spyne
RUN cd /python/spyne && python /python/spyne/setup.py install

ADD ./swhv-propagation/propaserv /python/propaserv
RUN cd /python/propaserv && python /python/propaserv/setup.py install

EXPOSE 7790
