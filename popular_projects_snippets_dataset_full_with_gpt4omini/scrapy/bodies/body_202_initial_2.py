class MockCredentials:# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return password == self.password.encode('utf8')# pragma: no cover
# pragma: no cover
credentials = MockCredentials(username=b'user', password=b'pass') # pragma: no cover
class MockPortal:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.username = b'user'# pragma: no cover
        self.password = b'pass'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {}# pragma: no cover
# pragma: no cover
portal = MockPortal() # pragma: no cover
telnet = type('MockTelnet', (object,), { 'TelnetBootstrapProtocol': lambda *args: None, 'TelnetTransport': lambda *args: None, 'AuthenticatingTelnetProtocol': type('MockProtocol', (object,), {}) })() # pragma: no cover
defers = lambda f: f # pragma: no cover
insults = type('MockInsults', (object,), { 'ServerProtocol': type('MockServerProtocol', (object,), {}) })() # pragma: no cover
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
