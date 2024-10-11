from twisted.internet.defer import Deferred # pragma: no cover
from twisted.conch import manhole, telnet, insults # pragma: no cover

def defers(f): # pragma: no cover
    def wrapper(*args, **kwargs): # pragma: no cover
        return Deferred() # pragma: no cover
    return wrapper # pragma: no cover
 # pragma: no cover
credentials = type('Mock', (object,), { # pragma: no cover
    'username': 'testuser', # pragma: no cover
    'checkPassword': lambda self, password: password == b'testpass' # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
mind = None # pragma: no cover
interfaces = [{}] # pragma: no cover

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
