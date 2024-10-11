from twisted.conch import telnet # pragma: no cover
from twisted.cred.checkers import ICredentialsChecker # pragma: no cover
from twisted.python.components import registerAdapter # pragma: no cover
from zope.interface import Interface # pragma: no cover

def defers(func): # pragma: no cover
    return func # pragma: no cover
 # pragma: no cover
class CredentialsMock: # pragma: no cover
    def __init__(self, username, password): # pragma: no cover
        self.username = username # pragma: no cover
        self.password = password # pragma: no cover
    def checkPassword(self, password): # pragma: no cover
        return self.password == password # pragma: no cover
 # pragma: no cover
class Portal: # pragma: no cover
    """An implementation of IPortal""" # pragma: no cover
    def __init__(self, username, password): # pragma: no cover
        self.username = username # pragma: no cover
        self.password = password # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
 # pragma: no cover
self = Portal(username='user', password='pass') # pragma: no cover
credentials = CredentialsMock(username='user', password='pass') # pragma: no cover
 # pragma: no cover
class MockTelnetBootstrapProtocol: # pragma: no cover
    def __init__(self, arg1, arg2, arg3): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockTelnetTransport: # pragma: no cover
    def __init__(self, arg1, arg2): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockAuthenticatingTelnetProtocol: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
telnet.TelnetBootstrapProtocol = MockTelnetBootstrapProtocol # pragma: no cover
telnet.TelnetTransport = MockTelnetTransport # pragma: no cover
telnet.AuthenticatingTelnetProtocol = MockAuthenticatingTelnetProtocol # pragma: no cover

from twisted.conch.telnet import TelnetTransport, AuthenticatingTelnetProtocol, TelnetBootstrapProtocol # pragma: no cover
from twisted.conch.insults import insults # pragma: no cover
from twisted.conch.manhole import Manhole # pragma: no cover
from twisted.cred.credentials import UsernamePassword # pragma: no cover
from twisted.internet.defer import inlineCallbacks as defers # pragma: no cover

class CredentialsMock: # pragma: no cover
    def __init__(self, username, password): # pragma: no cover
        self.username = username # pragma: no cover
        self.password = password # pragma: no cover
    def checkPassword(self, password): # pragma: no cover
        return self.password == password # pragma: no cover
 # pragma: no cover
credentials = CredentialsMock(username='user', password='pass') # pragma: no cover
 # pragma: no cover
class Portal: # pragma: no cover
    def __init__(self, username, password): # pragma: no cover
        self.username = username # pragma: no cover
        self.password = password # pragma: no cover
    @defers # pragma: no cover
    def login(self_, credentials, mind, *interfaces): # pragma: no cover
        if not ( # pragma: no cover
            credentials.username == self_.username.encode('utf8') # pragma: no cover
            and credentials.checkPassword(self_.password.encode('utf8')) # pragma: no cover
        ): # pragma: no cover
            raise ValueError("Invalid credentials") # pragma: no cover
        protocol = TelnetBootstrapProtocol( # pragma: no cover
            insults.ServerProtocol, # pragma: no cover
            Manhole, # pragma: no cover
            self_._get_telnet_vars() # pragma: no cover
        ) # pragma: no cover
        raise Exception((interfaces[0], protocol, lambda: None)) # pragma: no cover
 # pragma: no cover
    def _get_telnet_vars(self): # pragma: no cover
        return {} # pragma: no cover
 # pragma: no cover
self = Portal(username='user', password='pass') # pragma: no cover
telnet = type('MockTelnet', (object,), { 'TelnetTransport': TelnetTransport, 'AuthenticatingTelnetProtocol': AuthenticatingTelnetProtocol, 'TelnetBootstrapProtocol': TelnetBootstrapProtocol }) # pragma: no cover
insults = type('MockInsults', (object,), {'ServerProtocol': insults.ServerProtocol}) # pragma: no cover
manhole = type('MockManhole', (object,), {'Manhole': Manhole}) # pragma: no cover

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
