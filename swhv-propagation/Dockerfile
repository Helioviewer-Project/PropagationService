FROM python:3

COPY PropagationService /root/PropagationService
RUN cd /root/PropagationService/service && python ./setup.py install

EXPOSE 7790
