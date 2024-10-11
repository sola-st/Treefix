from typing import Any # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/772124/what-does-the-ellipsis-object-do
from l3.Runtime import _l_
class Foo:
    _l_(14780)

    bar: Any = ...
    _l_(14778)
    def __init__(self, name: str=...) -> None:
        _l_(14779)

...
