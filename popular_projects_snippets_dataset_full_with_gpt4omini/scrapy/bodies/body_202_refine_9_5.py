class MockCredentials: # pragma: no cover
    username = b'user'# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return password == b'pass' # pragma: no cover
credentials = MockCredentials() # pragma: no cover
class MockServerProtocol: pass # pragma: no cover
class MockManhole: pass # pragma: no cover
telnet = type('MockTelnet', (object,), {'TelnetBootstrapProtocol': lambda proto1, proto2, vars: None, 'TelnetTransport': lambda proto1, portal: None, 'AuthenticatingTelnetProtocol': None})() # pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': MockServerProtocol})() # pragma: no cover
manhole = type('MockManhole', (object,), {'Manhole': MockManhole})() # pragma: no cover
self = type('MockPortal', (object,), {'username': b'user', 'password': b'pass', '_get_telnet_vars': lambda self: {'key': 'value'}})() # pragma: no cover

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
