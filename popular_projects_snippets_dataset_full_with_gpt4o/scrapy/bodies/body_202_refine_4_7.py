import telnetlib as telnet # pragma: no cover
from twisted.internet.defer import Deferred as defers # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover

self = type('Mock', (object,), {'username': 'user', 'password': 'pass', '_get_telnet_vars': lambda self: {}})() # pragma: no cover

from twisted.cred.credentials import UsernamePassword # pragma: no cover
from twisted.conch import manhole # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover

class MockPortal: # pragma: no cover
    username = 'user' # pragma: no cover
    password = 'pass' # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
 # pragma: no cover
self = MockPortal() # pragma: no cover
credentials = type('MockCredentials', (object,), { # pragma: no cover
    'username': 'user', # pragma: no cover
    'password': 'pass', # pragma: no cover
    'checkPassword': lambda self, password: self.password == password # pragma: no cover
})() # pragma: no cover
insults.ServerProtocol = type('ServerProtocol', (object,), {}) # pragma: no cover
manhole.Manhole = type('Manhole', (object,), {}) # pragma: no cover

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
