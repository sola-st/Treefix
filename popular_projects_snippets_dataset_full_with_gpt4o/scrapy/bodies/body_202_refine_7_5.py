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

from twisted.internet import reactor # pragma: no cover
from twisted.conch import telnet # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
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
    return wrapper# pragma: no cover
 # pragma: no cover
class SelfMock:# pragma: no cover
    username = 'test_user'# pragma: no cover
    password = 'password123'# pragma: no cover
    def _get_telnet_vars(self):# pragma: no cover
        return {}# pragma: no cover
 # pragma: no cover
self = SelfMock()# pragma: no cover
 # pragma: no cover
class MockTelnetBootstrapProtocol:# pragma: no cover
    def __init__(self, arg1, arg2, arg3):# pragma: no cover
        pass# pragma: no cover
 # pragma: no cover
telnet.TelnetBootstrapProtocol = MockTelnetBootstrapProtocol# pragma: no cover
 # pragma: no cover
class MockTelnetTransport:# pragma: no cover
    def __init__(self, arg1, arg2):# pragma: no cover
        pass# pragma: no cover
 # pragma: no cover
telnet.TelnetTransport = MockTelnetTransport# pragma: no cover
 # pragma: no cover
class MockAuthenticatingTelnetProtocol:# pragma: no cover
    pass# pragma: no cover
 # pragma: no cover
telnet.AuthenticatingTelnetProtocol = MockAuthenticatingTelnetProtocol# pragma: no cover
 # pragma: no cover
insults.ServerProtocol = type('ServerProtocol', (object,), {})# pragma: no cover
 # pragma: no cover

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
