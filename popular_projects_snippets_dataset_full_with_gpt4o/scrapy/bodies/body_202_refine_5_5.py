from twisted.conch import telnet # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.internet.defer import Deferred as defers # pragma: no cover

self = type('Mock', (object,), {'username': 'user', 'password': 'pass', '_get_telnet_vars': lambda self: {}})() # pragma: no cover

from twisted.conch import telnet # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover
from twisted.internet.defer import returnValue # pragma: no cover

class Portal: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.username = 'user' # pragma: no cover
        self.password = 'pass' # pragma: no cover
 # pragma: no cover
    @defers # pragma: no cover
    def login(self_, credentials, mind, *interfaces): # pragma: no cover
        if not ( # pragma: no cover
            credentials.username == self.username.encode('utf8') # pragma: no cover
            and credentials.checkPassword(self.password.encode('utf8')) # pragma: no cover
        ): # pragma: no cover
            raise ValueError('Invalid credentials') # pragma: no cover
 # pragma: no cover
        protocol = telnet.TelnetBootstrapProtocol( # pragma: no cover
            insults.ServerProtocol, # pragma: no cover
            manhole.Manhole, # pragma: no cover
            self._get_telnet_vars() # pragma: no cover
        ) # pragma: no cover
        returnValue((interfaces[0], protocol, lambda: None)) # pragma: no cover
 # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
 # pragma: no cover
self = Portal() # pragma: no cover
 # pragma: no cover
class CredentialsMock: # pragma: no cover
    def __init__(self, username, password): # pragma: no cover
        self.username = username # pragma: no cover
        self.password = password # pragma: no cover
 # pragma: no cover
    def checkPassword(self, password): # pragma: no cover
        return self.password == password # pragma: no cover
 # pragma: no cover
credentials = CredentialsMock('user', 'pass') # pragma: no cover

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
