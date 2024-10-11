from typing import Any, Union, List # pragma: no cover
import token # pragma: no cover

class CannotTransform(Exception): pass # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error: Exception): # pragma: no cover
        self._error = error # pragma: no cover
    def err(self): # pragma: no cover
        return self._error # pragma: no cover
    def ok(self): # pragma: no cover
        return None # pragma: no cover
class Line: # pragma: no cover
    leaves: List[Any] # pragma: no cover
    def __init__(self, leaves: List[Any]): # pragma: no cover
        self.leaves = leaves # pragma: no cover
def mock_do_match(line: 'Line') -> Union[Err, Any]: # pragma: no cover
    return Err(CannotTransform('Mock matching error')) # pragma: no cover
def mock_do_transform(line: 'Line', indices: Any) -> List[Union[Err, Any]]: # pragma: no cover
    return [Err(CannotTransform('Mock transformation error'))] # pragma: no cover
MockStringTransformer = type('MockStringTransformer', (object,), { # pragma: no cover
    'do_match': mock_do_match, # pragma: no cover
    'do_transform': mock_do_transform # pragma: no cover
}) # pragma: no cover
line = Line([token.STRING]) # pragma: no cover
self = MockStringTransformer() # pragma: no cover

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
