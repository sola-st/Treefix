# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes
# decorators.py
from l3.Runtime import _l_
def abstract(f):
    _l_(1174)

    def _decorator(*_):
        _l_(1172)

        raise NotImplementedError(f"Method '{f.__name__}' is abstract")
        _l_(1171)
    aux = _decorator
    _l_(1173)
    return aux


# yourclass.py
class Vehicle:
    _l_(1179)

    def add_energy():
        _l_(1176)

        print("Energy added!")
        _l_(1175)

    @abstract
    def get_make():
        _l_(1177)

...
    @abstract
    def get_model():
        _l_(1178)

...
