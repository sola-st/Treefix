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

from twisted.cred.portal import IRealm, Portal # pragma: no cover
from twisted.cred.checkers import InMemoryUsernamePasswordDatabaseDontUse # pragma: no cover
from twisted.conch import manhole, insults # pragma: no cover
from twisted.conch.telnet import AuthenticatingTelnetProtocol, TelnetTransport, TelnetBootstrapProtocol # pragma: no cover
from twisted.internet import reactor, defer # pragma: no cover
from zope.interface import implementer # pragma: no cover

def defers(f):# pragma: no cover
    return defer.inlineCallbacks(f) # pragma: no cover
class MockCredentials:# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password# pragma: no cover
# pragma: no cover
credentials = MockCredentials('user', 'pass') # pragma: no cover
@implementer(IRealm)# pragma: no cover
class MockPortal:# pragma: no cover
    username = 'user'# pragma: no cover
    password = 'pass'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {}# pragma: no cover
    def requestAvatar(self, avatarId, mind, *interfaces):# pragma: no cover
        return telnet.ITelnetProtocol, None, lambda: None# pragma: no cover
self = MockPortal() # pragma: no cover
portal = Portal(MockPortal())# pragma: no cover
checker = InMemoryUsernamePasswordDatabaseDontUse()# pragma: no cover
checker.addUser('user', 'pass')# pragma: no cover
portal.registerChecker(checker) # pragma: no cover
manhole.Manhole = manhole.ColoredManhole # pragma: no cover

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
