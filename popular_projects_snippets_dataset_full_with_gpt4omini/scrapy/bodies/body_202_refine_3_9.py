class MockCredentials:# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password.decode('utf8')# pragma: no cover
# pragma: no cover
credentials = MockCredentials(username=b'testuser', password=b'testpass') # pragma: no cover
def mock_get_telnet_vars():# pragma: no cover
        return {'var1': 'value1', 'var2': 'value2'} # pragma: no cover
MockPortal = type('MockPortal', (object,), {'username': b'testuser', 'password': b'testpass', '_get_telnet_vars': mock_get_telnet_vars})# pragma: no cover
portal_instance = MockPortal() # pragma: no cover
class MockTelnetBootstrapProtocol:# pragma: no cover
    def __init__(self, protocol_class, manhole_class, variables):# pragma: no cover
        pass# pragma: no cover
class MockServerProtocol:# pragma: no cover
    pass# pragma: no cover
class MockManhole:# pragma: no cover
    pass# pragma: no cover
class MockAuthenticatingTelnetProtocol:# pragma: no cover
    pass# pragma: no cover
class MockTelnetTransport:# pragma: no cover
    def __init__(self, protocol_class, portal):# pragma: no cover
        pass# pragma: no cover

class MockCredentials:# pragma: no cover
    def __init__(self, username, password):# pragma: no cover
        self.username = username# pragma: no cover
        self.password = password# pragma: no cover
    def checkPassword(self, password):# pragma: no cover
        return self.password == password.decode('utf8')# pragma: no cover
# pragma: no cover
credentials = MockCredentials(username=b'testuser', password=b'testpass') # pragma: no cover
def mock_get_telnet_vars():# pragma: no cover
        return {'var1': 'value1', 'var2': 'value2'} # pragma: no cover
MockPortal = type('MockPortal', (object,), {'username': b'testuser', 'password': b'testpass', '_get_telnet_vars': mock_get_telnet_vars})() # pragma: no cover
class MockTelnetBootstrapProtocol:# pragma: no cover
    def __init__(self, protocol_class, manhole_class, variables):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
telnet = type('MockTelnet', (), {})()# pragma: no cover
telnet.TelnetBootstrapProtocol = MockTelnetBootstrapProtocol # pragma: no cover
class MockServerProtocol:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
insults = type('MockInsults', (), {})()# pragma: no cover
insults.ServerProtocol = MockServerProtocol # pragma: no cover
class MockManhole:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
manhole = type('MockManhole', (), {})()# pragma: no cover
manhole.Manhole = MockManhole # pragma: no cover
class MockAuthenticatingTelnetProtocol:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
telnet.AuthenticatingTelnetProtocol = MockAuthenticatingTelnetProtocol # pragma: no cover
class MockTelnetTransport:# pragma: no cover
    def __init__(self, protocol_class, portal):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
telnet.TelnetTransport = MockTelnetTransport # pragma: no cover
defers = lambda f: f # pragma: no cover

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
