# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8689964/why-do-some-functions-have-underscores-before-and-after-the-function-name
from l3.Runtime import _l_
class A:
    _l_(2596)

    def __init__(self, a):
        _l_(2593)

        self.a = a
        _l_(2592)
    def __custom__(self):
        _l_(2595)

        pass
        _l_(2594)

