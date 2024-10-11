from twisted.conch import manhole, telnet, insults # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

def defers(f):# pragma: no cover
    def wrapper(*args, **kwargs):# pragma: no cover
        d = Deferred()# pragma: no cover
        try:# pragma: no cover
            result = f(*args, **kwargs)# pragma: no cover
            d.callback(result)# pragma: no cover
        except Exception as e:# pragma: no cover
            d.errback(e)# pragma: no cover
        return d# pragma: no cover
    return wrapper # pragma: no cover
class SelfMock:# pragma: no cover
    username = 'test_user'# pragma: no cover
    password = 'password123'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {} # pragma: no cover
self = SelfMock() # pragma: no cover

from twisted.conch.telnet import AuthenticatingTelnetProtocol, TelnetTransport, TelnetBootstrapProtocol # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.conch.manhole import Manhole # pragma: no cover
from twisted.internet.defer import inlineCallbacks # pragma: no cover

def defers(f):# pragma: no cover
    return inlineCallbacks(f) # pragma: no cover
class MockPortal:# pragma: no cover
    username = 'user123'# pragma: no cover
    password = 'password123'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {} # pragma: no cover
self = MockPortal() # pragma: no cover
class MockCredentials:# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password # pragma: no cover
credentials = MockCredentials('user123', 'password123') # pragma: no cover
class MockTelnetTransport(TelnetTransport):# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass# pragma: no cover
    def write(self, data):# pragma: no cover
        print(data)# pragma: no cover
    def loseConnection(self):# pragma: no cover
        print('Connection closed')# pragma: no cover
    def logPrefix(self):# pragma: no cover
        return 'MockTelnetTransport' # pragma: no cover
TelnetTransport = MockTelnetTransport # pragma: no cover
class MockTelnetBootstrapProtocol(TelnetBootstrapProtocol):# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
TelnetBootstrapProtocol = MockTelnetBootstrapProtocol # pragma: no cover
class MockAuthenticatingTelnetProtocol(AuthenticatingTelnetProtocol):# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
AuthenticatingTelnetProtocol = MockAuthenticatingTelnetProtocol # pragma: no cover
class MockServerProtocol(insults.ServerProtocol):# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
insults.ServerProtocol = MockServerProtocol # pragma: no cover
class MockManhole(Manhole):# pragma: no cover
    def __init__(self, *args, **kwargs):# pragma: no cover
        pass # pragma: no cover
Manhole = MockManhole # pragma: no cover

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
