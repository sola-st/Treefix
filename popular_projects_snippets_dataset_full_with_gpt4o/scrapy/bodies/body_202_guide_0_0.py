from twisted.cred import checkers, credentials, portal # pragma: no cover
from twisted.conch import manhole, telnet, insults # pragma: no cover

class MockProtocol: # pragma: no cover
    pass # pragma: no cover
type('MockTelnetBootstrapProtocol', (object,), {}) # pragma: no cover
type('MockTelnetTransport', (object,), {}) # pragma: no cover
type('MockAuthenticatingTelnetProtocol', (object,), {}) # pragma: no cover
class MockCredentials: # pragma: no cover
    username = 'testuser' # pragma: no cover
    def checkPassword(self, password): # pragma: no cover
        return password == b'testpass' # pragma: no cover
mock_credentials = MockCredentials() # pragma: no cover
portal.Portal.username = 'testuser' # pragma: no cover
portal.Portal.password = 'testpass' # pragma: no cover
portal.Portal._get_telnet_vars = lambda self: {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/telnet.py
from l3.Runtime import _l_
class Portal:
    _l_(19457)

    """An implementation of IPortal"""
    @defers
    def login(self_, credentials, mind, *interfaces):
        _l_(19456)

        if not (
            credentials.username == self.username.encode('utf8')
            and credentials.checkPassword(self.password.encode('utf8'))
        ):
            _l_(19453)

            raise ValueError("Invalid credentials")
            _l_(19452)

        protocol = telnet.TelnetBootstrapProtocol(
            insults.ServerProtocol,
            manhole.Manhole,
            self._get_telnet_vars()
        )
        _l_(19454)
        aux = (interfaces[0], protocol, lambda: None)
        _l_(19455)
        exit(aux)
aux = telnet.TelnetTransport(
    telnet.AuthenticatingTelnetProtocol,
    Portal()
)
_l_(19458)

exit(aux)
