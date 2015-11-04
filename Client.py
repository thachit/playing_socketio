__author__ = 'thachnguyen'

from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class clientProtocol(LineReceiver):

    def __init__(self, factory):
        self.factory = factory

    def dataReceived(self, line):
        print "=>", str(line)

        print "* Input card: "
        user_input = raw_input()
        self.sendLine(str(user_input))

    def connectionMade(self):
        print "* Input card: "
        user_input = raw_input()
        self.sendLine(str(user_input))

    def sendLine(self, line):
        if line:
            return self.transport.write(line + self.delimiter)
        else:
            return None


class clientFactoryProtocol(ClientFactory):

    def buildProtocol(self, addr):
        return clientProtocol(self)


if __name__ == '__main__':
    reactor.connectTCP('localhost', int(6000),
                       clientFactoryProtocol(), timeout=60)
    reactor.run()