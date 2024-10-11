# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6618002/using-property-versus-getters-and-setters
from l3.Runtime import _l_
class Account(object):
    _l_(1059)

    @property
    def email(self):
        _l_(1054)

        aux = self._email
        _l_(1053)
        return aux

    @email.setter
    def email(self, value):
        _l_(1058)

        if '@' not in value:
            _l_(1056)

            raise ValueError('Invalid email address.')
            _l_(1055)
        self._email = value
        _l_(1057)

a = Account()
_l_(1060)
a.email = 'badaddress'
_l_(1061)

class Account(object):
    _l_(1066)

    ...
    _l_(1062)
    def validate(self):
        _l_(1065)

        if '@' not in self.email:
            _l_(1064)

            raise ValueError('Invalid email address.')
            _l_(1063)

