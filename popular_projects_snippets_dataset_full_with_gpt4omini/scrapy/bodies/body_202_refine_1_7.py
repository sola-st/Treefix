class MockCredentials:# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password.decode('utf8')# pragma: no cover
# pragma: no cover
credentials = MockCredentials(b'example_user', b'secure_password') # pragma: no cover
telnet = type('MockTelnet', (), {})()# pragma: no cover
telnet.TelnetBootstrapProtocol = lambda a, b, c: 'TelnetBootstrapProtocolInstance'# pragma: no cover
telnet.TelnetTransport = lambda a, b: 'TelnetTransportInstance'# pragma: no cover
telnet.AuthenticatingTelnetProtocol = 'AuthenticatingTelnetProtocol' # pragma: no cover
defers = lambda f: f # pragma: no cover
class MockPortal:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.username = b'example_user'# pragma: no cover
        self.password = b'secure_password'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {'var1': 'value1'}# pragma: no cover
# pragma: no cover
Portal = MockPortal() # pragma: no cover
insults = type('MockInsults', (), {})()# pragma: no cover
insults.ServerProtocol = 'ServerProtocol' # pragma: no cover
manhole = type('MockManhole', (), {})()# pragma: no cover
manhole.Manhole = 'Manhole' # pragma: no cover

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
