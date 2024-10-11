from __future__ import annotations # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes
# decorators.py
from l3.Runtime import _l_
def abstract(f):
    _l_(13632)

    def _decorator(*_):
        _l_(13630)

        raise NotImplementedError(f"Method '{f.__name__}' is abstract")
        _l_(13629)
    aux = _decorator
    _l_(13631)
    return aux


# yourclass.py
class Vehicle:
    _l_(13637)

    def add_energy():
        _l_(13634)

        print("Energy added!")
        _l_(13633)

    @abstract
    def get_make():
        _l_(13635)

...
    @abstract
    def get_model():
        _l_(13636)

...
