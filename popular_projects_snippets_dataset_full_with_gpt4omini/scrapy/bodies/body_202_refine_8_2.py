self = type('MockPortal', (object,), {'username': b'testuser', 'password': b'testpass', '_get_telnet_vars': lambda self: {}})() # pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': object})() # pragma: no cover
manhole = type('MockManhole', (object,), {})() # pragma: no cover

class MockCredentials:# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
    # pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password.decode('utf8')# pragma: no cover
# pragma: no cover
credentials = MockCredentials(b'test_user', b'test_pass') # pragma: no cover
defers = lambda f: f# pragma: no cover
 # pragma: no cover
self = type('MockPortal', (object,), {'username': b'test_user', 'password': b'test_pass', '_get_telnet_vars': lambda self: {}})() # pragma: no cover
class MockServerProtocol:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': MockServerProtocol})() # pragma: no cover
class MockManhole:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
manhole = type('MockManhole', (object,), {})() # pragma: no cover
telnet = type('MockTelnet', (object,), {})()# pragma: no cover
telnet.TelnetBootstrapProtocol = lambda proto1, proto2, vars: None# pragma: no cover
telnet.TelnetTransport = lambda proto, portal: None# pragma: no cover
telnet.AuthenticatingTelnetProtocol = lambda: None # pragma: no cover

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
