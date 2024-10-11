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
        return self.password == password.decode('utf8')# pragma: no cover
# pragma: no cover
credentials = MockCredentials(b'user', b'pass') # pragma: no cover
defers = lambda func: func # pragma: no cover
class MockPortal:# pragma: no cover
    username = b'user'# pragma: no cover
    password = b'pass'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {}# pragma: no cover
# pragma: no cover
portal_instance = MockPortal() # pragma: no cover
telnet = type('MockTelnet', (object,), {})()# pragma: no cover
telnet.TelnetBootstrapProtocol = lambda a, b, c: 'TelnetBootstrapProtocolInstance'# pragma: no cover
telnet.TelnetTransport = lambda a, b: 'TelnetTransportInstance'# pragma: no cover
telnet.AuthenticatingTelnetProtocol = 'AuthenticatingTelnetProtocol' # pragma: no cover
class MockInsults:# pragma: no cover
    class ServerProtocol: pass# pragma: no cover
insults = MockInsults() # pragma: no cover
class MockManhole: pass# pragma: no cover
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
