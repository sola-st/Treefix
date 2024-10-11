Cheese = type('Cheese', (object,), {'num_holes': 0}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-implement-multiple-constructors
from l3.Runtime import _l_
class Gouda(Cheese):
    _l_(3230)

    def __init__(self):
        _l_(3229)

        super(Gouda).__init__(num_holes=10)
        _l_(3228)


class Parmesan(Cheese):
    _l_(3233)

    def __init__(self):
        _l_(3232)

        super(Parmesan).__init__(num_holes=15) 
        _l_(3231) 

