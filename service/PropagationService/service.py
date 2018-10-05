
import logging
logging.basicConfig(level=logging.INFO)

from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import Service
from spyne.model.primitive import AnyDict, Float, Unicode

from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument

from spyne.server.wsgi import WsgiApplication

from spyne.util.six.moves.urllib.request import Request, urlopen

import json

#####

server = 'http://127.0.0.1:7789/json/position?'

fixed_speed = 1000.
observer = 'SUN'
target = 'SOHO'
ref = 'HEEQ'

def add_speed(response):
    ret = json.load(response)
    result = ret['result']

    for item in result:
        for v in item.values():
            v.append(fixed_speed)
    return ret

class PropagationService(Service):
    @srpc(Unicode(min_occurs=1), Unicode(min_occurs=1),
          Unicode(min_occurs=0), Float(min_occurs=0),
          _returns=AnyDict)
    def propagation(name, utc, utc_end, deltat):
        utc_end_req = '' if utc_end is None else '&utc_end=' + utc_end
        deltat_req = '' if deltat is None else '&deltat=' + deltat

        url = server + 'utc=' + utc + '&observer=' + observer + '&target=' + target + '&ref=' + ref + utc_end_req + deltat_req

        request = Request(url)
        response = urlopen(request)
        return add_speed(response)

#####

def propagation_service(fcgi=True):
    if fcgi is False:
        def _on_method_return_object(ctx):
            ctx.transport.resp_headers['Access-Control-Allow-Origin'] = "*"
            ctx.transport.resp_headers['Cache-Control'] = "public,max-age=86400" # tbd

        PropagationService.event_manager.add_listener('method_return_object',
                                                      _on_method_return_object)

    json = Application([PropagationService], tns='swhv.service.propagation',
                       in_protocol=HttpRpc(validator='soft'),
                       out_protocol=JsonDocument())

    return WsgiApplication(json)
