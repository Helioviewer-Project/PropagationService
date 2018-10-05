#!/usr/bin/env python

from flup.server.fcgi_fork import WSGIServer
from PropagationService import service

WSGIServer(service.propagation_service()).run()
