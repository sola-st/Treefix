from twisted.conch import telnet, insults, manhole # pragma: no cover
from twisted.internet import defer # pragma: no cover
from twisted.cred.credentials import UsernamePassword # pragma: no cover

def defers(f):# pragma: no cover
    return defer.inlineCallbacks(f) # pragma: no cover
class MockPortal:# pragma: no cover
    username = 'testuser'# pragma: no cover
    password = 'testpassword'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {}# pragma: no cover
self = MockPortal() # pragma: no cover
telnet = type('MockTelnet', (object,), { 'TelnetTransport': telnet.TelnetTransport, 'AuthenticatingTelnetProtocol': telnet.AuthenticatingTelnetProtocol, 'TelnetBootstrapProtocol': telnet.TelnetBootstrapProtocol }) # pragma: no cover
manhole = type('MockManhole', (object,), {'Manhole': manhole.Manhole}) # pragma: no cover

from twisted.conch import telnet, insults, manhole # pragma: no cover
from twisted.internet import defer # pragma: no cover

class MockCredentials:# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password# pragma: no cover
credentials = MockCredentials('testuser', 'testpassword') # pragma: no cover
def defers(f):# pragma: no cover
    return defer.inlineCallbacks(f) # pragma: no cover
class MockPortal:# pragma: no cover
    username = 'testuser'# pragma: no cover
    password = 'testpassword'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {}# pragma: no cover
self = MockPortal() # pragma: no cover
telnet = type('MockTelnet', (object,), {# pragma: no cover
    'TelnetTransport': telnet.TelnetTransport,# pragma: no cover
    'AuthenticatingTelnetProtocol': telnet.AuthenticatingTelnetProtocol,# pragma: no cover
    'TelnetBootstrapProtocol': lambda *args: args# pragma: no cover
}) # pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': object}) # pragma: no cover
manhole = type('MockManhole', (object,), {'Manhole': object}) # pragma: no cover

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
