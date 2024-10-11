class Account(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self._email = '' # pragma: no cover
    @property # pragma: no cover
    def email(self): # pragma: no cover
        aux = self._email # pragma: no cover
        return aux # pragma: no cover
    @email.setter # pragma: no cover
    def email(self, value): # pragma: no cover
        if '@' not in value: # pragma: no cover
            raise ValueError('Invalid email address.') # pragma: no cover
        self._email = value # pragma: no cover
class Account(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self._email = 'valid@example.com' # pragma: no cover
    @property # pragma: no cover
    def email(self): # pragma: no cover
        return self._email # pragma: no cover
    @email.setter # pragma: no cover
    def email(self, value): # pragma: no cover
        if '@' not in value: # pragma: no cover
            raise ValueError('Invalid email address.') # pragma: no cover
        self._email = value # pragma: no cover
    def validate(self): # pragma: no cover
        if '@' not in self.email: # pragma: no cover
            raise ValueError('Invalid email address.') # pragma: no cover
 # pragma: no cover
try: # pragma: no cover
    a = Account() # pragma: no cover
    a.email = 'badaddress' # pragma: no cover
except ValueError as e: # pragma: no cover
    print(e) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618002/using-property-versus-getters-and-setters
from l3.Runtime import _l_
class Account(object):
    _l_(12659)

    @property
    def email(self):
        _l_(12654)

        aux = self._email
        _l_(12653)
        return aux

    @email.setter
    def email(self, value):
        _l_(12658)

        if '@' not in value:
            _l_(12656)

            raise ValueError('Invalid email address.')
            _l_(12655)
        self._email = value
        _l_(12657)

a = Account()
_l_(12660)
a.email = 'badaddress'
_l_(12661)

class Account(object):
    _l_(12666)

    ...
    _l_(12662)
    def validate(self):
        _l_(12665)

        if '@' not in self.email:
            _l_(12664)

            raise ValueError('Invalid email address.')
            _l_(12663)

