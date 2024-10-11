class accum:  # Define the class again to fix the SyntaxError # pragma: no cover
    def __init__(self): # pragma: no cover
        self.acc = 0 # pragma: no cover
    def accumulator(self, var2add, end): # pragma: no cover
        if not end: # pragma: no cover
            self.acc += var2add # pragma: no cover
        return self.acc # pragma: no cover
self = accum() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
from l3.Runtime import _l_
class accum:
    _l_(2070)

    def __init__(self):
        _l_(2065)

        self.acc = 0
        _l_(2064)
    def accumulator(self, var2add, end):
        _l_(2068)

        if not end:
            _l_(2067)

            self.acc+=var2add
            _l_(2066)
    aux = self.acc
    _l_(2069)
    return aux

