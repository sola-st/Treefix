from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet import protocol # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

self = type('Mock', (object,), { '_connectBuffer': b'', '_protocol': type('MockProtocol', (object,), { 'transport': type('MockTransport', (object,), { 'startTLS': lambda self, sslOptions, protocolFactory: None })(), 'dataReceived': None })(), '_protocolDataReceived': None, '_contextFactory': ClientContextFactory(), '_tunneledHost': 'example.com', '_tunneledPort': 443, '_protocolFactory': None, '_tunnelReadyDeferred': Deferred(), '_truncatedLength': 10, '_host': 'proxy.example.com', '_port': 8080 })() # pragma: no cover
rcvd_bytes = b'HTTP/1.1 200 Connection Established\r\n\r\n' # pragma: no cover
TunnelingTCP4ClientEndpoint = type('MockTunnelingTCP4ClientEndpoint', (object,), { '_responseMatcher': type('MockResponseMatcher', (object,), { 'match': lambda self, buffer: re.match(r'^(?P<status>\d+) (?P<reason>.*)$', buffer.decode()) })() }) # pragma: no cover

import re # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover
from twisted.internet import protocol # pragma: no cover
from twisted.internet.ssl import ClientContextFactory # pragma: no cover

self = type('Mock', (object,), { '_connectBuffer': b'', '_protocol': type('MockProtocol', (object,), { 'transport': type('MockTransport', (object,), { 'startTLS': lambda self, sslOptions, protocolFactory: None })(), 'dataReceived': None })(), '_protocolDataReceived': None, '_contextFactory': ClientContextFactory(), '_tunneledHost': 'example.com', '_tunneledPort': 443, '_protocolFactory': None, '_tunnelReadyDeferred': Deferred(), '_truncatedLength': 10, '_host': 'proxy.example.com', '_port': 8080 })() # pragma: no cover
rcvd_bytes = b'HTTP/1.1 200 Connection Established\r\n\r\n' # pragma: no cover
TunnelingTCP4ClientEndpoint = type('MockTunnelingTCP4ClientEndpoint', (object,), { '_responseMatcher': type('MockResponseMatcher', (object,), { 'match': lambda self, buffer: re.match(rb'^(?P<status>\d+) (?P<reason>.*)$', buffer) })() })() # pragma: no cover
TunnelError = Exception # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
from l3.Runtime import _l_
"""Processes the response from the proxy. If the tunnel is successfully
        created, notifies the client that we are ready to send requests. If not
        raises a TunnelError.
        """
self._connectBuffer += rcvd_bytes
_l_(5442)
# make sure that enough (all) bytes are consumed
# and that we've got all HTTP headers (ending with a blank line)
# from the proxy so that we don't send those bytes to the TLS layer
#
# see https://github.com/scrapy/scrapy/issues/2491
if b'\r\n\r\n' not in self._connectBuffer:
    _l_(5444)

    exit()
    _l_(5443)
self._protocol.dataReceived = self._protocolDataReceived
_l_(5445)
respm = TunnelingTCP4ClientEndpoint._responseMatcher.match(self._connectBuffer)
_l_(5446)
if respm and int(respm.group('status')) == 200:
    _l_(5454)

    # set proper Server Name Indication extension
    sslOptions = self._contextFactory.creatorForNetloc(self._tunneledHost, self._tunneledPort)
    _l_(5447)
    self._protocol.transport.startTLS(sslOptions, self._protocolFactory)
    _l_(5448)
    self._tunnelReadyDeferred.callback(self._protocol)
    _l_(5449)
else:
    if respm:
        _l_(5452)

        extra = {'status': int(respm.group('status')),
                 'reason': respm.group('reason').strip()}
        _l_(5450)
    else:
        extra = rcvd_bytes[:self._truncatedLength]
        _l_(5451)
    self._tunnelReadyDeferred.errback(
        TunnelError('Could not open CONNECT tunnel with proxy '
                    f'{self._host}:{self._port} [{extra!r}]')
    )
    _l_(5453)
