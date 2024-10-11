from twisted.internet import reactor # pragma: no cover
from twisted.cred import credentials # pragma: no cover
from twisted.python import log # pragma: no cover
from twisted.internet.endpoints import TCP4ClientEndpoint # pragma: no cover

class MockCredentials:  # Needed to mock the credentials object # pragma: no cover
    def __init__(self, username, password): # pragma: no cover
        self.username = username.encode('utf8') # pragma: no cover
        self.password = password # pragma: no cover
 # pragma: no cover
    def checkPassword(self, password): # pragma: no cover
        return self.password == password # pragma: no cover
 # pragma: no cover
class MockProtocol: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Portal: # pragma: no cover
    username = 'user' # pragma: no cover
# Assuming some values for username and password # pragma: no cover
    password = 'pass' # pragma: no cover
# Assuming some values for username and password # pragma: no cover
 # pragma: no cover
    def login(self_, credentials, mind, *interfaces): # pragma: no cover
        if not ( # pragma: no cover
            credentials.username == self.username.encode('utf8') # pragma: no cover
            and credentials.checkPassword(self.password.encode('utf8')) # pragma: no cover
        ): # pragma: no cover
            raise ValueError('Invalid credentials') # pragma: no cover
        protocol = telnet.TelnetBootstrapProtocol( # pragma: no cover
            MockProtocol, # pragma: no cover
            None, # pragma: no cover
            {}, # pragma: no cover
        ) # pragma: no cover
        aux = (interfaces[0], protocol, lambda: None) # pragma: no cover
cred = MockCredentials('user', 'pass') # pragma: no cover
portal = Portal() # pragma: no cover

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
