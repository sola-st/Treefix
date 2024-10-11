telnet = type('MockTelnet', (object,), {})() # pragma: no cover
telnet.TelnetBootstrapProtocol = type('MockTelnetBootstrapProtocol', (object,), {}) # pragma: no cover
telnet.TelnetTransport = type('MockTelnetTransport', (object,), {}) # pragma: no cover
telnet.AuthenticatingTelnetProtocol = type('MockAuthenticatingTelnetProtocol', (object,), {}) # pragma: no cover
self = type('MockPortal', (object,), {'username': b'user', 'password': b'pass', '_get_telnet_vars': lambda self: {}})() # pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': object})() # pragma: no cover
manhole = type('MockManhole', (object,), {})() # pragma: no cover

class MockCredentials:# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password # pragma: no cover
credentials = MockCredentials(b'testuser', b'testpass') # pragma: no cover
defers = lambda func: func # pragma: no cover
class MockPortal:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.username = b'testuser'# pragma: no cover
        self.password = b'testpass'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {'var1': 'value1'} # pragma: no cover
Portal = MockPortal() # pragma: no cover
class MockTelnetBootstrapProtocol:# pragma: no cover
    def __init__(self, protocol_class, manhole_class, telnet_vars):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
telnet = type('MockTelnet', (), {# pragma: no cover
    'TelnetBootstrapProtocol': MockTelnetBootstrapProtocol,# pragma: no cover
    'TelnetTransport': lambda p, portal: 'TelnetTransportInstance',# pragma: no cover
    'AuthenticatingTelnetProtocol': 'AuthenticatingTelnetProtocol'# pragma: no cover
})() # pragma: no cover
class MockInsults:# pragma: no cover
    class ServerProtocol: pass# pragma: no cover
# pragma: no cover
insults = MockInsults() # pragma: no cover
class MockManhole:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
manhole = MockManhole() # pragma: no cover

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
