# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
from l3.Runtime import _l_
class MyException(Exception):
    _l_(12767)

    pass
    _l_(12766)

raise MyException("My hovercraft is full of eels")
_l_(12768)

raise MyException({"message":"My hovercraft is full of animals", "animal":"eels"})
_l_(12769)

try:
    _l_(12774)

    raise MyException({"message":"My hovercraft is full of animals", "animal":"eels"})
    _l_(12770)
except MyException as e:
    _l_(12773)

    details = e.args[0]
    _l_(12771)
    print(details["animal"])
    _l_(12772)

class MyError(Exception):
    _l_(12780)

    def __init__(self, message, animal):
        _l_(12777)

        self.message = message
        _l_(12775)
        self.animal = animal
        _l_(12776)
    def __str__(self):
        _l_(12779)

        aux = self.message
        _l_(12778)
        return aux

