telnet = type('MockTelnet', (object,), {})() # pragma: no cover
telnet.TelnetBootstrapProtocol = type('MockTelnetBootstrapProtocol', (object,), {}) # pragma: no cover
telnet.TelnetTransport = type('MockTelnetTransport', (object,), {}) # pragma: no cover
telnet.AuthenticatingTelnetProtocol = type('MockAuthenticatingTelnetProtocol', (object,), {}) # pragma: no cover
self = type('MockPortal', (object,), {'username': b'user', 'password': b'pass', '_get_telnet_vars': lambda self: {}})() # pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': object})() # pragma: no cover
manhole = type('MockManhole', (object,), {})() # pragma: no cover

class MockCredentials:# pragma: no cover
    username = b'test_user'# pragma: no cover
    password = b'test_password'# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return password == self.password# pragma: no cover
# pragma: no cover
credentials = MockCredentials() # pragma: no cover
defers = lambda func: func # pragma: no cover
class MockPortal:# pragma: no cover
    username = b'test_user'# pragma: no cover
    password = b'test_password'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {'var1': 'value1'}# pragma: no cover
# pragma: no cover
portal_instance = MockPortal() # pragma: no cover
class MockTelnetBootstrapProtocol:# pragma: no cover
    def __init__(self, proto1, proto2, vars): pass# pragma: no cover
# pragma: no cover
telnet = type('MockTelnet', (object,), {'TelnetBootstrapProtocol': MockTelnetBootstrapProtocol})() # pragma: no cover
class MockServerProtocol:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': MockServerProtocol})() # pragma: no cover
class MockManhole:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
manhole = type('MockManhole', (object,), {'Manhole': MockManhole})() # pragma: no cover
class MockTelnetTransport:# pragma: no cover
    def __init__(self, proto1, portal): pass# pragma: no cover
# pragma: no cover
telnet.TelnetTransport = MockTelnetTransport # pragma: no cover
class MockAuthenticatingTelnetProtocol:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
telnet.AuthenticatingTelnetProtocol = MockAuthenticatingTelnetProtocol # pragma: no cover

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
