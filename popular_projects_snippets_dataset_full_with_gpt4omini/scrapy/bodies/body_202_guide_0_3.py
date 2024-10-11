from twisted.internet import reactor # pragma: no cover
from twisted.conch import manhole # pragma: no cover
from twisted.conch import insults # pragma: no cover

class Credentials:  # Mock implementation# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password.decode('utf8')# pragma: no cover
# pragma: no cover
credentials = Credentials(username='testuser', password='testpass') # pragma: no cover
def telnet_authenticating_protocol():# pragma: no cover
    pass  # Mock implementation# pragma: no cover

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
