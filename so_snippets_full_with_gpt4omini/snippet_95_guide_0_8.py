MyException = type('MyException', (Exception,), {}) # pragma: no cover
MyError = type('MyError', (Exception,), {'__init__': lambda self, message, animal: setattr(self, 'message', message) or setattr(self, 'animal', animal), '__str__': lambda self: self.message}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
from l3.Runtime import _l_
class MyException(Exception):
    _l_(881)

    pass
    _l_(880)

raise MyException("My hovercraft is full of eels")
_l_(882)

raise MyException({"message":"My hovercraft is full of animals", "animal":"eels"})
_l_(883)

try:
    _l_(888)

    raise MyException({"message":"My hovercraft is full of animals", "animal":"eels"})
    _l_(884)
except MyException as e:
    _l_(887)

    details = e.args[0]
    _l_(885)
    print(details["animal"])
    _l_(886)

class MyError(Exception):
    _l_(894)

    def __init__(self, message, animal):
        _l_(891)

        self.message = message
        _l_(889)
        self.animal = animal
        _l_(890)
    def __str__(self):
        _l_(893)

        aux = self.message
        _l_(892)
        return aux

