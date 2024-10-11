from typing import List, Any, Union # pragma: no cover
from unittest.mock import Mock # pragma: no cover

line = type('Line', (object,), {'leaves': []})() # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover
self = type('MockSelf', (object,), {'do_match': Mock(), 'do_transform': Mock()})() # pragma: no cover
Err = type('Err', (object,), {'err': Mock()}) # pragma: no cover
token = type('Token', (object,), {'STRING': 'STRING'}) # pragma: no cover

from typing import List, Any # pragma: no cover
from unittest.mock import Mock # pragma: no cover

line = type('Line', (object,), {'leaves': [type('Leaf', (object,), {'type': 'STRING'})()]})() # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error_message): # pragma: no cover
        self._error_message = error_message # pragma: no cover
    def err(self): # pragma: no cover
        return CannotTransform(self._error_message) # pragma: no cover
class MatchResultOk: # pragma: no cover
    def ok(self): # pragma: no cover
        return [0] # pragma: no cover
line_match_result = MatchResultOk() # pragma: no cover
line_transform_result_ok = type('LineTransformResultOk', (object,), {'ok': lambda self: 'transformed_line'})() # pragma: no cover
line_transform_result_err = Err('Transformation error') # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    'do_match': lambda self, line: line_match_result, # pragma: no cover
    'do_transform': lambda self, line, indices: [line_transform_result_ok, line_transform_result_err] # pragma: no cover
})() # pragma: no cover
token = type('Token', (object,), {'STRING': 'STRING'}) # pragma: no cover

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
