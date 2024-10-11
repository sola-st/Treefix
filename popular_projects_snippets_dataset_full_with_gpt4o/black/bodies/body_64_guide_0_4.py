from typing import Any, List # pragma: no cover
import token # pragma: no cover

class CannotTransform(Exception): pass # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, err: Exception): # pragma: no cover
        self._err = err # pragma: no cover
    def err(self): # pragma: no cover
        return self._err # pragma: no cover
class MockMatchResult: # pragma: no cover
    def __init__(self, is_error: bool = False): # pragma: no cover
        self.is_error = is_error # pragma: no cover
    def ok(self): # pragma: no cover
        return [0] if not self.is_error else None # pragma: no cover
    def err(self): # pragma: no cover
        return CannotTransform('Mock error') if self.is_error else None # pragma: no cover
line = type('MockLine', (object,), {'leaves': [type('Leaf', (object,), {'type': token.STRING})()]}) # pragma: no cover
self = type('MockTransformer', (object,), { # pragma: no cover
    'do_match': lambda self, line: MockMatchResult(is_error=True), # pragma: no cover
    'do_transform': lambda self, line, indices: iter([Err(CannotTransform('Mock transformation error'))]) # pragma: no cover
})() # pragma: no cover
exit = lambda x: print('Exiting with:', x) # pragma: no cover

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
