from typing import Any # pragma: no cover

class Cheese: # pragma: no cover
    def __init__(self, num_holes: Any): # pragma: no cover
        self.num_holes = num_holes # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-implement-multiple-constructors
from l3.Runtime import _l_
class Gouda(Cheese):
    _l_(15286)

    def __init__(self):
        _l_(15285)

        super(Gouda).__init__(num_holes=10)
        _l_(15284)


class Parmesan(Cheese):
    _l_(15289)

    def __init__(self):
        _l_(15288)

        super(Parmesan).__init__(num_holes=15) 
        _l_(15287) 

