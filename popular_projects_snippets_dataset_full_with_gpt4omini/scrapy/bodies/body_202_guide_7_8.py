from twisted.internet import reactor # pragma: no cover
from twisted.conch import manhole # pragma: no cover
from twisted.conch import insults # pragma: no cover
from twisted.cred import credentials # pragma: no cover

class MockCredentials: # pragma: no cover
    def __init__(self, username, password): # pragma: no cover
        self.username = username.encode('utf8') # pragma: no cover
        self.password = password.encode('utf8') # pragma: no cover
 # pragma: no cover
    def checkPassword(self, password): # pragma: no cover
        return self.password == password # pragma: no cover
 # pragma: no cover
class MockPortal: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.username = 'user' # pragma: no cover
        self.password = 'pass' # pragma: no cover
    def _get_telnet_vars(self): return {'var': 'value'} # pragma: no cover
 # pragma: no cover
    def login(self_, credentials, mind, *interfaces): # pragma: no cover
        if not ( # pragma: no cover
            credentials.username == self.username.encode('utf8') # pragma: no cover
            and credentials.checkPassword(self.password.encode('utf8')) # pragma: no cover
        ): # pragma: no cover
            raise ValueError('Invalid credentials') # pragma: no cover
        protocol = telnet.TelnetBootstrapProtocol( # pragma: no cover
            insults.ServerProtocol, # pragma: no cover
            manhole.Manhole, # pragma: no cover
            self._get_telnet_vars() # pragma: no cover
        ) # pragma: no cover
        aux = (interfaces[0], protocol, lambda: None) # pragma: no cover
 # pragma: no cover
portal_instance = MockPortal() # pragma: no cover
credentials = MockCredentials('user', 'pass') # pragma: no cover
interfaces = [object()] # pragma: no cover

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
