import logging
logging.basicConfig(level=logging.DEBUG)

from spyne.application import Application
from spyne.decorator import rpc
from spyne.service import ServiceBase
from spyne.model.primitive import AnyDict, Integer, Float, String
from spyne import Array

from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.protocol.msgpack import MessagePackDocument

from spyne.server.wsgi import WsgiApplication

#####

class SolarSystemPropagationService(ServiceBase):
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

        SolarSystemPropagationService.event_manager.add_listener('method_return_object',
                                                              _on_method_return_object)

    tns = 'sidc.service.propagation'

    json = Application([SolarSystemPropagationService], tns=tns,
                       in_protocol=JsonDocument(validator='soft'),
                       out_protocol=JsonDocument())
    return WsgiApplication(json)
