from zope.interface import Interface # pragma: no cover
from twisted.conch import telnet # pragma: no cover
from twisted.conch.telnet import AuthenticatingTelnetProtocol # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.cred.checkers import InMemoryUsernamePasswordDatabaseDontUse # pragma: no cover
from twisted.cred.credentials import UsernamePassword # pragma: no cover
from twisted.internet.defer import succeed as defers # pragma: no cover

UserDatabase = InMemoryUsernamePasswordDatabaseDontUse() # pragma: no cover
UserDatabase.addUser(b'admin', b'adminpass') # pragma: no cover
credentials = UsernamePassword(b'admin', b'adminpass') # pragma: no cover
class MockPortal: # pragma: no cover
    username = 'admin' # pragma: no cover
    password = 'adminpass' # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
mock_portal = MockPortal() # pragma: no cover

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
