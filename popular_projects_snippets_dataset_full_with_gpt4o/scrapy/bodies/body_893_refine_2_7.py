import re # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
rcvd_bytes = b'HTTP/1.1 200 Connection Established\r\n\r\n' # pragma: no cover
TunnelingTCP4ClientEndpoint = type('Mock', (object,), {'_responseMatcher': re.compile(br'HTTP/1.1 (?P<status>\d{3}) (?P<reason>.+)\r\n')}) # pragma: no cover
TunnelError = type('TunnelError', (Exception,), {}) # pragma: no cover
self._connectBuffer = b'' # pragma: no cover
self._protocol = type('Mock', (object,), {'dataReceived': None, 'transport': type('Transport', (object,), {'startTLS': lambda sslOptions, protocolFactory: None})()})() # pragma: no cover
self._protocolDataReceived = lambda data: None # pragma: no cover
self._contextFactory = type('Mock', (object,), {'creatorForNetloc': lambda host, port: None})() # pragma: no cover
self._tunneledHost = 'example.com' # pragma: no cover
self._tunneledPort = 443 # pragma: no cover
self._protocolFactory = None # pragma: no cover
self._tunnelReadyDeferred = type('Mock', (object,), {'callback': lambda protocol: None, 'errback': lambda error: None})() # pragma: no cover
self._truncatedLength = 50 # pragma: no cover
self._host = 'proxy.example.com' # pragma: no cover
self._port = 8080 # pragma: no cover

import re # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
rcvd_bytes = b'HTTP/1.1 200 Connection Established\r\n\r\n' # pragma: no cover
TunnelingTCP4ClientEndpoint = type('Mock', (object,), {'_responseMatcher': re.compile(br'HTTP/1.1 (?P<status>\d{3}) (?P<reason>.+)\r\n')})() # pragma: no cover
TunnelError = type('TunnelError', (Exception,), {}) # pragma: no cover
self._connectBuffer = b'' # pragma: no cover
self._protocol = type('Mock', (object,), {'dataReceived': None, 'transport': type('Transport', (object,), {'startTLS': lambda sslOptions, factory: None})()})() # pragma: no cover
self._protocolDataReceived = lambda data: None # pragma: no cover
self._contextFactory = type('MockContextFactory', (ClientContextFactory,), {'creatorForNetloc': lambda self, host, port: None})() # pragma: no cover
self._tunneledHost = 'example.com' # pragma: no cover
self._tunneledPort = 443 # pragma: no cover
self._protocolFactory = None # pragma: no cover
self._tunnelReadyDeferred = Deferred() # pragma: no cover
self._truncatedLength = 10 # pragma: no cover
self._host = 'proxy.example.com' # pragma: no cover
self._port = 8080 # pragma: no cover

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
