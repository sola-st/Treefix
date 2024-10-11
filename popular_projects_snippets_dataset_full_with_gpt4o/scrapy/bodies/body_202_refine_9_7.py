from twisted.conch import manhole, insults # pragma: no cover
from twisted.conch.telnet import TelnetTransport, AuthenticatingTelnetProtocol, TelnetBootstrapProtocol # pragma: no cover
from twisted.cred.credentials import UsernamePassword # pragma: no cover
from twisted.internet import defer # pragma: no cover

telnet = type('telnet', (), {'TelnetTransport': TelnetTransport, 'AuthenticatingTelnetProtocol': AuthenticatingTelnetProtocol, 'TelnetBootstrapProtocol': TelnetBootstrapProtocol}) # pragma: no cover
defers = defer.inlineCallbacks # pragma: no cover

from twisted.conch import manhole, insults # pragma: no cover
from twisted.conch.telnet import TelnetTransport, AuthenticatingTelnetProtocol, TelnetBootstrapProtocol # pragma: no cover
from twisted.cred.credentials import UsernamePassword # pragma: no cover
from twisted.internet import defer # pragma: no cover

def defers(f): # pragma: no cover
    return defer.inlineCallbacks(f) # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    username = 'user' # pragma: no cover
    password = 'password' # pragma: no cover
    @staticmethod # pragma: no cover
    def _get_telnet_vars(): # pragma: no cover
        return {} # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

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
