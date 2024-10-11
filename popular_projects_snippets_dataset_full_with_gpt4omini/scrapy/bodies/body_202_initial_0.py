from twisted.internet import defer # pragma: no cover
from twisted.internet import protocol # pragma: no cover

defers = defer.deferredGenerator # pragma: no cover
self = type('MockPortal', (object,), {'username': b'test_user', 'password': b'test_password', '_get_telnet_vars': lambda self: {}})() # pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': type('MockServerProtocol', (protocol.Protocol,), {})})() # pragma: no cover
manhole = type('MockManhole', (object,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/telnet.py
from l3.Runtime import _l_
class Portal:
    _l_(8234)

    """An implementation of IPortal"""
    @defers
    def login(self_, credentials, mind, *interfaces):
        _l_(8233)

        if not (
            credentials.username == self.username.encode('utf8')
            and credentials.checkPassword(self.password.encode('utf8'))
        ):
            _l_(8230)

            raise ValueError("Invalid credentials")
            _l_(8229)

        protocol = telnet.TelnetBootstrapProtocol(
            insults.ServerProtocol,
            manhole.Manhole,
            self._get_telnet_vars()
        )
        _l_(8231)
        aux = (interfaces[0], protocol, lambda: None)
        _l_(8232)
        exit(aux)
aux = telnet.TelnetTransport(
    telnet.AuthenticatingTelnetProtocol,
    Portal()
)
_l_(8235)

exit(aux)
