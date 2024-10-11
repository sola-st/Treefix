# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
from l3.Runtime import _l_
class MyClass:
    _l_(12487)

    @classmethod
    def make_new(cls) -> __qualname__:
        _l_(12486)

        aux = cls()
        _l_(12485)
        return aux

