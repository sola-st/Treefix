from typing import List, Union, Any # pragma: no cover

class CannotTransform(Exception):# pragma: no cover
    pass # pragma: no cover
line = type('MockLine', (object,), {'leaves': [type('Leaf', (object,), {'type': token.STRING})()]})() # pragma: no cover
Err = type('Err', (object,), {'__init__': lambda self, err: setattr(self, '_err', err), 'err': lambda self: self._err}) # pragma: no cover
self = type('MockSelf', (object,), {# pragma: no cover
    'do_match': lambda self, line: type('Result', (object,), {# pragma: no cover
        'ok': lambda: [0],# pragma: no cover
        'err': None# pragma: no cover
    })(),# pragma: no cover
    'do_transform': lambda self, line, indices: [type('Result', (object,), {# pragma: no cover
        'ok': lambda: line,# pragma: no cover
        'err': None# pragma: no cover
    })()]})() # pragma: no cover

from typing import List, Union # pragma: no cover

token = type('MockToken', (object,), {'STRING': 'STRING'}) # pragma: no cover
 # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, type): # pragma: no cover
        self.type = type # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self, leaves: List[Leaf]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
 # pragma: no cover
line = Line(leaves=[Leaf(type=token.STRING)]) # pragma: no cover
 # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error: Exception): # pragma: no cover
        self._error = error # pragma: no cover
    def err(self) -> Exception: # pragma: no cover
        return self._error # pragma: no cover
 # pragma: no cover
class Ok: # pragma: no cover
    pass
 # pragma: no cover
class StringTransformer: # pragma: no cover
    def do_match(self, line: Line) -> Union[Ok, Err]: # pragma: no cover
        return Ok([0]) # pragma: no cover
 # pragma: no cover
self = StringTransformer() # pragma: no cover

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
