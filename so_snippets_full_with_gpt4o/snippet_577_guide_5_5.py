# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8689964/why-do-some-functions-have-underscores-before-and-after-the-function-name
from l3.Runtime import _l_
class A:
    _l_(14813)

    def __init__(self, a):
        _l_(14810)

        self.a = a
        _l_(14809)
    def __custom__(self):
        _l_(14812)

        pass
        _l_(14811)

