#!/usr/bin/env python

#import os
#os.putenv('OPENBLAS_MAIN_FREE', '1')

#from wsgiref.simple_server import make_server
from werkzeug.serving import run_simple

# stop stupid reverse DNS lookup / not sure if still needed
# __import__('BaseHTTPServer').BaseHTTPRequestHandler.address_string = lambda x:x.client_address[0]

from propaserv import service

#####
# http://pylonsbook.com/en/1.1/the-web-server-gateway-interface-wsgi.html#altering-the-response

import gzip, io

class GzipMiddleware(object):
    def __init__(self, app, compresslevel=9):
        self.app = app
        self.compresslevel = compresslevel

    def __call__(self, environ, start_response):
        if 'gzip' not in environ.get('HTTP_ACCEPT_ENCODING', ''):
            return self.app(environ, start_response)

        buffer = io.BytesIO()
        output = gzip.GzipFile(
            mode='wb',
            compresslevel=self.compresslevel,
            fileobj=buffer
        )

        start_response_args = []
        def dummy_start_response(status, headers, exc_info=None):
            start_response_args.append(status)
            start_response_args.append(headers)
            start_response_args.append(exc_info)
            return output.write

        app_iter = self.app(environ, dummy_start_response)
        for line in app_iter:
            output.write(line)
        if hasattr(app_iter, 'close'):
            app_iter.close()
        output.close()
        buffer.seek(0)
        result = buffer.getvalue()
        headers = []
        for name, value in start_response_args[1]:
            if name.lower() != 'content-length':
                 headers.append((name, value))
        headers.append(('Content-Length', str(len(result))))
        headers.append(('Content-Encoding', 'gzip'))
        start_response(start_response_args[0], headers, start_response_args[2])
        buffer.close()
        return [result]

#####

gzip_app = GzipMiddleware(service.propagation_service(False), compresslevel=1)
run_simple('0.0.0.0', 7789, gzip_app, threaded=True)
