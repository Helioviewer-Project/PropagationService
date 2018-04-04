#!/usr/bin/env python

from flup.server.fcgi_fork import WSGIServer
from propaserv import service

WSGIServer(service.propagation_service()).run()
