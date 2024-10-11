from twisted.cred import portal, credentials # pragma: no cover
from twisted.conch import manhole, telnet # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from zope.interface import implementer # pragma: no cover
from twisted.python import log # pragma: no cover

defers = lambda func: func # pragma: no cover
telnet.TelnetTransport = type('TelnetTransport', (object,), {}) # pragma: no cover
telnet.AuthenticatingTelnetProtocol = type('AuthenticatingTelnetProtocol', (object,), {}) # pragma: no cover
telnet.TelnetBootstrapProtocol = type('TelnetBootstrapProtocol', (object,), {}) # pragma: no cover
insults.ServerProtocol = type('ServerProtocol', (object,), {}) # pragma: no cover
manhole.Manhole = type('Manhole', (object,), {}) # pragma: no cover
class SelfMock: # pragma: no cover
    username = 'user' # pragma: no cover
    password = 'pass' # pragma: no cover
    def _get_telnet_vars(self): return {} # pragma: no cover
self = SelfMock() # pragma: no cover

from twisted.cred import portal, credentials # pragma: no cover
from twisted.conch import manhole, telnet # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover

class MockTelnetTransport(telnet.TelnetTransport): # pragma: no cover
    def __init__(self, protocolFactory, portal): # pragma: no cover
        self.protocolFactory = protocolFactory # pragma: no cover
        self.portal = portal # pragma: no cover
 # pragma: no cover
class MockAuthenticatingTelnetProtocol(telnet.AuthenticatingTelnetProtocol): # pragma: no cover
    def __init__(self, portal): # pragma: no cover
        self.portal = portal # pragma: no cover
 # pragma: no cover
class MockTelnetBootstrapProtocol(telnet.TelnetBootstrapProtocol): # pragma: no cover
    def __init__(self, args1, args2, args3): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
telnet.TelnetTransport = MockTelnetTransport # pragma: no cover
telnet.AuthenticatingTelnetProtocol = MockAuthenticatingTelnetProtocol # pragma: no cover
telnet.TelnetBootstrapProtocol = MockTelnetBootstrapProtocol # pragma: no cover
insults.ServerProtocol = type('ServerProtocol', (object,), {}) # pragma: no cover
manhole.Manhole = type('Manhole', (object,), {}) # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'username': 'user', # pragma: no cover
    'password': 'pass', # pragma: no cover
    '_get_telnet_vars': lambda self: {} # pragma: no cover
})() # pragma: no cover

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
