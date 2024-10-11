import re # pragma: no cover
from unittest.mock import Mock # pragma: no cover

TunnelError = type('TunnelError', (Exception,), {}) # pragma: no cover

import re # pragma: no cover
from unittest.mock import Mock # pragma: no cover

class SelfMock: # pragma: no cover
    _connectBuffer = b'' # pragma: no cover
    _protocol = Mock() # pragma: no cover
    _protocolDataReceived = Mock() # pragma: no cover
    _contextFactory = Mock() # pragma: no cover
    _tunneledHost = 'example.com' # pragma: no cover
    _tunneledPort = 443 # pragma: no cover
    _protocolFactory = Mock() # pragma: no cover
    _tunnelReadyDeferred = Mock() # pragma: no cover
    _truncatedLength = 10 # pragma: no cover
    _host = 'proxy.example.com' # pragma: no cover
    _port = 8080 # pragma: no cover
self = SelfMock() # pragma: no cover
rcvd_bytes = b'HTTP/1.1 200 Connection Established\r\n\r\n' # pragma: no cover
TunnelingTCP4ClientEndpoint = type('TunnelingTCP4ClientEndpointMock', (object,), {'_responseMatcher': re.compile(br'HTTP/1.1 (?P<status>\d{3}) (?P<reason>.+)\r\n')})() # pragma: no cover
TunnelError = type('TunnelError', (Exception,), {}) # pragma: no cover
self._protocol.transport = Mock() # pragma: no cover
self._protocol.transport.startTLS = lambda sslOptions, protocolFactory: None # pragma: no cover
self._contextFactory.creatorForNetloc = lambda host, port: Mock() # pragma: no cover
self._tunnelReadyDeferred.callback = lambda protocol: None # pragma: no cover
self._tunnelReadyDeferred.errback = lambda error: None # pragma: no cover

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
