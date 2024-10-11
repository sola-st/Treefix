import re # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

class MockProtocol: # pragma: no cover
    def transport(self): # pragma: no cover
        return self # pragma: no cover
    def startTLS(self, sslOptions, protocolFactory): # pragma: no cover
        pass # pragma: no cover
    def dataReceived(self, data): # pragma: no cover
        pass # pragma: no cover
_protocol = MockProtocol() # pragma: no cover
_protocolDataReceived = MockProtocol().dataReceived # pragma: no cover
_connectBuffer = b'' # pragma: no cover
_tunneledHost = 'examplehost' # pragma: no cover
_tunneledPort = 1234 # pragma: no cover
_truncatedLength = 10 # pragma: no cover
_host = 'proxyhost' # pragma: no cover
_port = 8080 # pragma: no cover
_contextFactory = type('ContextFactory', (object,), {'creatorForNetloc': lambda self, host, port: None})() # pragma: no cover
_protocolFactory = None # pragma: no cover
_tunnelReadyDeferred = Deferred() # pragma: no cover
TunnelingTCP4ClientEndpoint = type('TunnelingTCP4ClientEndpoint', (object,), {'_responseMatcher': re.compile(rb'HTTP/(?P<version>\d+\.\d+) (?P<status>\d{3}) (?P<reason>.+)\r\n')}) # pragma: no cover
self = type('Mock', (object,), {'_protocol': _protocol, '_protocolDataReceived': _protocolDataReceived, '_connectBuffer': _connectBuffer, '_tunneledHost': _tunneledHost, '_tunneledPort': _tunneledPort, '_truncatedLength': _truncatedLength, '_host': _host, '_port': _port, '_contextFactory': _contextFactory, '_protocolFactory': _protocolFactory, '_tunnelReadyDeferred': _tunnelReadyDeferred})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
"""Processes the response from the proxy. If the tunnel is successfully
        created, notifies the client that we are ready to send requests. If not
        raises a TunnelError.
        """
self._connectBuffer += rcvd_bytes
_l_(17065)
# make sure that enough (all) bytes are consumed
# and that we've got all HTTP headers (ending with a blank line)
# from the proxy so that we don't send those bytes to the TLS layer
#
# see https://github.com/scrapy/scrapy/issues/2491
if b'\r\n\r\n' not in self._connectBuffer:
    _l_(17067)

    exit()
    _l_(17066)
self._protocol.dataReceived = self._protocolDataReceived
_l_(17068)
respm = TunnelingTCP4ClientEndpoint._responseMatcher.match(self._connectBuffer)
_l_(17069)
if respm and int(respm.group('status')) == 200:
    _l_(17077)

    # set proper Server Name Indication extension
    sslOptions = self._contextFactory.creatorForNetloc(self._tunneledHost, self._tunneledPort)
    _l_(17070)
    self._protocol.transport.startTLS(sslOptions, self._protocolFactory)
    _l_(17071)
    self._tunnelReadyDeferred.callback(self._protocol)
    _l_(17072)
else:
    if respm:
        _l_(17075)

        extra = {'status': int(respm.group('status')),
                 'reason': respm.group('reason').strip()}
        _l_(17073)
    else:
        extra = rcvd_bytes[:self._truncatedLength]
        _l_(17074)
    self._tunnelReadyDeferred.errback(
        TunnelError('Could not open CONNECT tunnel with proxy '
                    f'{self._host}:{self._port} [{extra!r}]')
    )
    _l_(17076)
