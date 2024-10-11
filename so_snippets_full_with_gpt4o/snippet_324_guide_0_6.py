a = type('Mock', (object,), {'_email': ''})() # pragma: no cover

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

