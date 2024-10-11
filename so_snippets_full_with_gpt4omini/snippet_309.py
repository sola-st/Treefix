# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/772124/what-does-the-ellipsis-object-do
from l3.Runtime import _l_
class Foo:
    _l_(3050)

    bar: Any = ...
    _l_(3048)
    def __init__(self, name: str=...) -> None:
        _l_(3049)

...
