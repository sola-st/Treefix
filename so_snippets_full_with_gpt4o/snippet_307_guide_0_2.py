import types # pragma: no cover

MockGuineaPig = type('GuineaPig', (object,), {}) # pragma: no cover
MockGorilla = type('Gorilla', (object,), {'patch': lambda cls: (lambda fn: fn)}) # pragma: no cover
guineapig = MockGuineaPig() # pragma: no cover
gorilla = MockGorilla() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance
from l3.Runtime import _l_
try:
    import gorilla
    _l_(13216)

except ImportError:
    pass
try:
    import guineapig
    _l_(13218)

except ImportError:
    pass
@gorilla.patch(guineapig)
def needle():
    _l_(13220)

    print("awesome")
    _l_(13219)

