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
from twisted.conch import telnet, manhole # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover
from twisted.python import log # pragma: no cover

class SelfMock: # pragma: no cover
    username = 'user' # pragma: no cover
    password = 'pass' # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
self = SelfMock() # pragma: no cover
telnet.TelnetTransport = type('TelnetTransport', (object,), {'__init__': lambda self, protocol, factory: None}) # pragma: no cover
telnet.AuthenticatingTelnetProtocol = type('AuthenticatingTelnetProtocol', (object,), {}) # pragma: no cover
telnet.TelnetBootstrapProtocol = type('TelnetBootstrapProtocol', (object,), {'__init__': lambda self, arg1, arg2, arg3: None}) # pragma: no cover
insults.ServerProtocol = type('ServerProtocol', (object,), {'__init__': lambda self, *args, **kwargs: None}) # pragma: no cover
manhole.Manhole = type('Manhole', (object,), {'__init__': lambda self, *args, **kwargs: None}) # pragma: no cover
credentials = type('Credentials', (object,), {'username': 'user', 'checkPassword': lambda self, password: self.password == password}) # pragma: no cover

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
