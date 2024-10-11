from typing import Any, Dict, List # pragma: no cover
import token # pragma: no cover

line = type('MockLine', (object,), {'leaves': [type('MockLeaf', (object,), {'type': token.STRING})()]})() # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover
self = type('MockTransformer', (object,), {'do_match': lambda self, line: type('OkErr', (object,), {'ok': lambda: [0], 'err': lambda: None})()})() # pragma: no cover
Err = type('Err', (object,), {'err': lambda self: None}) # pragma: no cover
token.STRING = 3 # pragma: no cover
self.do_transform = lambda self, line, indices: [type('OkErr', (object,), {'ok': lambda: line, 'err': lambda: None})()] # pragma: no cover
self.__class__.__name__ = 'MockTransformer' # pragma: no cover

from typing import List # pragma: no cover
import token # pragma: no cover

line = type('MockLine', (object,), { # pragma: no cover
    'leaves': [type('MockLeaf', (object,), {'type': token.STRING})()] # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error): # pragma: no cover
        self._error = error # pragma: no cover
     # pragma: no cover
    def err(self): # pragma: no cover
        return self._error # pragma: no cover
 # pragma: no cover
class OkErr: # pragma: no cover
    def __init__(self, ok_val=None, err_val=None): # pragma: no cover
        self._ok_val = ok_val # pragma: no cover
        self._err_val = err_val # pragma: no cover
 # pragma: no cover
    def ok(self): # pragma: no cover
        return self._ok_val # pragma: no cover
 # pragma: no cover
    def err(self): # pragma: no cover
        return self._err_val # pragma: no cover
 # pragma: no cover
self = type('MockTransformer', (object,), { # pragma: no cover
    'do_match': lambda self, line: OkErr(ok_val=[0]), # pragma: no cover
    'do_transform': lambda self, line, indices: [OkErr(ok_val=line)], # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
token.STRING = 'string' # pragma: no cover

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
