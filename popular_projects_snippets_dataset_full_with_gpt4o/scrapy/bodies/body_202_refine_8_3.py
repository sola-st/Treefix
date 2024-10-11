import telnetlib as telnet # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover

self = type('Mock', (object,), {'username': 'user', 'password': 'pass', '_get_telnet_vars': lambda self: {}})() # pragma: no cover
self.username = 'user' # pragma: no cover
self.password = 'pass' # pragma: no cover
telnet.TelnetBootstrapProtocol = type('Mock', (object,), {'__init__': lambda self, *args, **kwargs: None})() # pragma: no cover
insults.ServerProtocol = type('Mock', (object,), {'__init__': lambda self, *args, **kwargs: None})() # pragma: no cover
self._get_telnet_vars = lambda: {} # pragma: no cover
telnet.TelnetTransport = type('Mock', (object,), {'__init__': lambda self, *args, **kwargs: None})() # pragma: no cover
telnet.AuthenticatingTelnetProtocol = type('Mock', (object,), {'__init__': lambda self, *args, **kwargs: None})() # pragma: no cover

from twisted.cred import portal # pragma: no cover
from twisted.conch.telnet import TelnetTransport, AuthenticatingTelnetProtocol, TelnetBootstrapProtocol # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.conch.manhole import Manhole # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover
import sys # pragma: no cover

class SelfMock: # pragma: no cover
    username = 'user' # pragma: no cover
    password = 'password123' # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
self = SelfMock() # pragma: no cover

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
