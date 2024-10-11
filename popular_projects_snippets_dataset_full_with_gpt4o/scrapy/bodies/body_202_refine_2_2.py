from twisted.cred.credentials import UsernamePassword # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from functools import partial # pragma: no cover

defers = partial # pragma: no cover
class MockPortal(type('Mock', (object,), {})): pass # pragma: no cover
self = MockPortal() # pragma: no cover
self.username = 'user' # pragma: no cover
self.password = 'pass' # pragma: no cover
insults.ServerProtocol = type('ServerProtocol', (object,), {}) # pragma: no cover
def _get_telnet_vars(): return {} # pragma: no cover
self._get_telnet_vars = _get_telnet_vars # pragma: no cover

from twisted.conch import manhole # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover

class MockCredentials: # pragma: no cover
    def __init__(self, username, password): # pragma: no cover
        self.username = username # pragma: no cover
        self.password = password # pragma: no cover
    def checkPassword(self, password): # pragma: no cover
        return self.password == password # pragma: no cover
credentials = MockCredentials('user', 'pass') # pragma: no cover
class MockPortal: # pragma: no cover
    username = 'user' # pragma: no cover
    password = 'pass' # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
self = MockPortal() # pragma: no cover
class MockTelnetBootstrapProtocol: # pragma: no cover
    def __init__(self, *args, **kwargs): pass # pragma: no cover
class MockServerProtocol: # pragma: no cover
    def __init__(self, *args, **kwargs): pass # pragma: no cover
insults.ServerProtocol = MockServerProtocol # pragma: no cover
class MockManhole: # pragma: no cover
    def __init__(self, *args, **kwargs): pass # pragma: no cover
manhole.Manhole = MockManhole # pragma: no cover
class MockTelnetTransport: # pragma: no cover
    def __init__(self, *args, **kwargs): pass # pragma: no cover
class MockAuthenticatingTelnetProtocol: # pragma: no cover
    def __init__(self, *args, **kwargs): pass # pragma: no cover

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
