import re # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet.error import ConnectError # pragma: no cover

class TunnelError(ConnectError): pass # pragma: no cover
 # pragma: no cover
class MockTransport: # pragma: no cover
    def startTLS(self, sslOptions, protocolFactory): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockProtocol: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.transport = MockTransport() # pragma: no cover
        self.dataReceived = None # pragma: no cover
 # pragma: no cover
class MockContextFactory: # pragma: no cover
    def creatorForNetloc(self, host, port): # pragma: no cover
        return 'sslOptions' # pragma: no cover
 # pragma: no cover
class MockResponseMatcher: # pragma: no cover
    def match(self, buffer): # pragma: no cover
        return re.match(br'HTTP/1.1 (?P<status>[0-9]{3}) (?P<reason>[^\r\n]+)\r\n', buffer) # pragma: no cover
 # pragma: no cover
TunnelingTCP4ClientEndpoint = type('TunnelingTCP4ClientEndpoint', (object,), { '_responseMatcher': MockResponseMatcher() }) # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_connectBuffer': b'HTTP/1.1 500 Internal Server Error\r\n\r\n', # pragma: no cover
    '_protocol': MockProtocol(), # pragma: no cover
    '_protocolDataReceived': lambda data: None, # pragma: no cover
    '_contextFactory': MockContextFactory(), # pragma: no cover
    '_protocolFactory': None, # pragma: no cover
    '_tunnelReadyDeferred': Deferred(), # pragma: no cover
    '_tunneledHost': 'example.com', # pragma: no cover
    '_tunneledPort': 443, # pragma: no cover
    '_host': 'proxy.example.com', # pragma: no cover
    '_port': 8080, # pragma: no cover
    '_truncatedLength': 10 # pragma: no cover
}) # pragma: no cover
 # pragma: no cover
rcvd_bytes = b'HTTP/1.1 500 Internal Server Error\r\n\r\n' # pragma: no cover

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
