from typing import Any, List # pragma: no cover
from types import SimpleNamespace # pragma: no cover

line = SimpleNamespace(leaves=[SimpleNamespace(type='STRING')]) # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover
Err = type('Err', (object,), {'__init__': lambda self, err: setattr(self, 'err', err), 'err': lambda self: self.err}) # pragma: no cover
token = SimpleNamespace(STRING='STRING') # pragma: no cover
self = type('Mock', (object,), {'do_match': lambda self, line: SimpleNamespace(ok=lambda: [1], err=lambda: None), 'do_transform': lambda self, line, string_indices: [SimpleNamespace(ok=lambda: line, err=lambda: None)], '__class__': type('MockClass', (object,), {})})() # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, type_: int): # pragma: no cover
        self.type = type_ # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self, leaves: List[Leaf]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
line = Line(leaves=[Leaf(type_=token.STRING)]) # pragma: no cover
 # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error: Exception): # pragma: no cover
        self._error = error # pragma: no cover
    def err(self) -> Exception: # pragma: no cover
        return self._error # pragma: no cover
 # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, value: Any): # pragma: no cover
        self._value = value # pragma: no cover
    def ok(self) -> Any: # pragma: no cover
        return self._value # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def do_match(self, line: Line) -> Ok: # pragma: no cover
        return Ok([0]) # pragma: no cover
 # pragma: no cover
    def do_transform(self, line: Line, indices: List[int]) -> List[Ok]: # pragma: no cover
        return [Ok(line)] # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        StringTransformer instances have a call signature that mirrors that of
        the Transformer type.

        Raises:
            CannotTransform(...) if the concrete StringTransformer class is unable
            to transform @line.
        """
# Optimization to avoid calling `self.do_match(...)` when the line does
# not contain any string.
if not any(leaf.type == token.STRING for leaf in line.leaves):
    _l_(17914)

    raise CannotTransform("There are no strings in this line.")
    _l_(17913)

match_result = self.do_match(line)
_l_(17915)

if isinstance(match_result, Err):
    _l_(17918)

    cant_transform = match_result.err()
    _l_(17916)
    raise CannotTransform(
        f"The string transformer {self.__class__.__name__} does not recognize"
        " this line as one that it can transform."
    ) from cant_transform
    _l_(17917)

string_indices = match_result.ok()
_l_(17919)

for line_result in self.do_transform(line, string_indices):
    _l_(17925)

    if isinstance(line_result, Err):
        _l_(17922)

        cant_transform = line_result.err()
        _l_(17920)
        raise CannotTransform(
            "StringTransformer failed while attempting to transform string."
        ) from cant_transform
        _l_(17921)
    line = line_result.ok()
    _l_(17923)
    aux = line
    _l_(17924)
    exit(aux)
