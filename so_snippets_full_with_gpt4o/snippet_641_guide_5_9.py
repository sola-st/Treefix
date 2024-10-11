class ModifiedAccum:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.acc = 0 # pragma: no cover
    def accumulator(self, var2add, end): # pragma: no cover
        if not end: # pragma: no cover
            self.acc += var2add # pragma: no cover
        return self.acc # pragma: no cover
modified_instance = ModifiedAccum() # pragma: no cover
result = modified_instance.accumulator(10, False) # This will add 10 to acc and return 10 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
from l3.Runtime import _l_
class accum:
    _l_(12732)

    def __init__(self):
        _l_(12727)

        self.acc = 0
        _l_(12726)
    def accumulator(self, var2add, end):
        _l_(12730)

        if not end:
            _l_(12729)

            self.acc+=var2add
            _l_(12728)
    aux = self.acc
    _l_(12731)
    return aux

