from typing import List, Union # pragma: no cover
class Err: pass # pragma: no cover
class CannotTransform(Exception): pass # pragma: no cover

token = type('MockToken', (), {'STRING': 'string'})() # pragma: no cover
line = type('MockLine', (), {'leaves': [type('MockLeaf', (), {'type': token.STRING})()]})() # pragma: no cover
self = type('MockStringTransformer', (), {'do_match': lambda self, line: type('MockResult', (), {'ok': lambda: [0, 1], 'err': lambda: None})(), '__class__': type('Mock', (object,), {})})() # pragma: no cover
Err = type('MockErr', (), {'__init__': lambda self: None, 'err': lambda self: 'error occurred'}) # pragma: no cover

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
    _l_(6187)

    raise CannotTransform("There are no strings in this line.")
    _l_(6186)

match_result = self.do_match(line)
_l_(6188)

if isinstance(match_result, Err):
    _l_(6191)

    cant_transform = match_result.err()
    _l_(6189)
    raise CannotTransform(
        f"The string transformer {self.__class__.__name__} does not recognize"
        " this line as one that it can transform."
    ) from cant_transform
    _l_(6190)

string_indices = match_result.ok()
_l_(6192)

for line_result in self.do_transform(line, string_indices):
    _l_(6198)

    if isinstance(line_result, Err):
        _l_(6195)

        cant_transform = line_result.err()
        _l_(6193)
        raise CannotTransform(
            "StringTransformer failed while attempting to transform string."
        ) from cant_transform
        _l_(6194)
    line = line_result.ok()
    _l_(6196)
    aux = line
    _l_(6197)
    exit(aux)
