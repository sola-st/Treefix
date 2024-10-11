from twisted.cred.credentials import UsernamePassword # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.conch.manhole import Manhole # pragma: no cover
from twisted.conch.telnet import TelnetBootstrapProtocol, TelnetTransport, AuthenticatingTelnetProtocol # pragma: no cover

class MockSelf: # pragma: no cover
    username = 'user' # pragma: no cover
    password = 'pass' # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
class MockCredentials: # pragma: no cover
    username = 'user' # pragma: no cover
    def checkPassword(self, password): # pragma: no cover
        return password == b'pass' # pragma: no cover
credentials = MockCredentials() # pragma: no cover
 # pragma: no cover
mind = None # pragma: no cover
interfaces = [object()] # pragma: no cover

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
