class Credentials:# pragma: no cover
    username = b'user'# pragma: no cover
    password = b'pass'# pragma: no cover
# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password # pragma: no cover
credentials = Credentials() # pragma: no cover
defers = lambda f: f # pragma: no cover
class MockPortal:# pragma: no cover
    username = b'user'# pragma: no cover
    password = b'pass'# pragma: no cover
# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {'key': 'value'} # pragma: no cover
self = MockPortal() # pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': object})() # pragma: no cover
manhole = type('MockManhole', (object,), {})() # pragma: no cover
telnet = type('MockTelnet', (object,), {})()# pragma: no cover
telnet.TelnetBootstrapProtocol = lambda x, y, z: None# pragma: no cover
telnet.TelnetTransport = lambda x, y: None# pragma: no cover
telnet.AuthenticatingTelnetProtocol = object # pragma: no cover

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
