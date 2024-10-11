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

from twisted.conch import telnet # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover

class SelfMock: # pragma: no cover
    username = 'user' # pragma: no cover
    password = 'pass' # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
self = SelfMock() # pragma: no cover
class MockTelnetBootstrapProtocol: # pragma: no cover
    def __init__(self, arg1, arg2, arg3): # pragma: no cover
        pass # pragma: no cover
telnet.TelnetBootstrapProtocol = MockTelnetBootstrapProtocol # pragma: no cover
class MockTelnetTransport: # pragma: no cover
    def __init__(self, protocol, portal): # pragma: no cover
        self.protocol = protocol # pragma: no cover
        self.portal = portal # pragma: no cover
telnet.TelnetTransport = MockTelnetTransport # pragma: no cover
class MockAuthenticatingTelnetProtocol: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
telnet.AuthenticatingTelnetProtocol = MockAuthenticatingTelnetProtocol # pragma: no cover
class MockServerProtocol: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover
insults.ServerProtocol = MockServerProtocol # pragma: no cover
class MockManhole: # pragma: no cover
    def __init__(self): # pragma: no cover
        pass # pragma: no cover

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
