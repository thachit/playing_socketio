__author__ = 'thachnguyen'


from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.web.websockets import WebSocketsProtocolWrapper, WebSocketsResource, lookupProtocolForFactory
from twisted.web.server import Site
from twisted.internet import reactor

TCP_PORT = 6000
WEBSOCKET_PORT = 6060
HTTP_PORT = 6080

class serverProtocol(LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def dataReceived(self, data):
        print data
        for web_client in self.factory.Webclients:
            web_client.sendLine(data)

        self.sendLine(data)


    def connectionMade(self):
        if isinstance(self.transport, WebSocketsProtocolWrapper):
            self.factory.Webclients.append(self)  # Add Web client to Clients param


class serverFactoryProtocol(Factory):
    service = None
    Webclients = []

    def buildProtocol(self, addr):
        print "Connect from client: ", addr
        return serverProtocol(self)


def run():
    factory = serverFactoryProtocol()
    reactor.listenTCP(TCP_PORT, factory)

    # Config HTTP
    from http import app
    from twisted.web.wsgi import WSGIResource
    resource = WSGIResource(reactor, reactor.getThreadPool(), app)
    reactor.listenTCP(HTTP_PORT, Site(resource))

    # Config Websocket
    ws_resource = WebSocketsResource(lookupProtocolForFactory(factory))
    reactor.listenTCP(WEBSOCKET_PORT, Site(ws_resource))

    reactor.run()

if __name__ == '__main__':
    run()
