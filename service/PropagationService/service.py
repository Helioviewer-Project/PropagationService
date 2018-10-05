
import logging
logging.basicConfig(level=logging.INFO)

from spyne.application import Application
from spyne.decorator import rpc
from spyne.service import Service
from spyne.model.primitive import Integer
from spyne import Array

from spyne.protocol.json import JsonDocument

from spyne.server.wsgi import WsgiApplication

#####

class PropagationService(Service):
    @rpc(Array(Integer), Integer,
         _returns=Array(Integer))
    def time_shift(ctx, needs_shift, shift):
        for i in range(len(needs_shift)):
            needs_shift[i] = needs_shift[i] + shift
        return needs_shift
#####

def propagation_service(fcgi=True):
    if fcgi is False:
        def _on_method_return_object(ctx):
            ctx.transport.resp_headers['Access-Control-Allow-Origin'] = "*"
            ctx.transport.resp_headers['Cache-Control'] = "public,max-age=86400" # tbd

        PropagationService.event_manager.add_listener('method_return_object',
                                                      _on_method_return_object)

    tns = 'swhv.service.propagation'

    json = Application([PropagationService], tns=tns,
                       in_protocol=JsonDocument(validator='soft'),
                       out_protocol=JsonDocument())

    return WsgiApplication(json)
