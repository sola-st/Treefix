import token # pragma: no cover
from typing import Union # pragma: no cover

class CannotTransform(Exception): pass # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, err): # pragma: no cover
        self._err = err # pragma: no cover
    def err(self): # pragma: no cover
        return self._err # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, ok): # pragma: no cover
        self._ok = ok # pragma: no cover
    def ok(self): # pragma: no cover
        return self._ok # pragma: no cover
class MockStringTransformer(type('Mock', (object,), {})): # pragma: no cover
    def do_match(self, line): # pragma: no cover
        return Err('Mock match error.') # pragma: no cover
    def do_transform(self, line, string_indices): # pragma: no cover
        yield Ok('Transformed line') # pragma: no cover
self = MockStringTransformer() # pragma: no cover
line = type('Line', (object,), {'leaves': [{'type': token.STRING}]})() # pragma: no cover
exit = lambda x: print('Exit called with:', x) # pragma: no cover

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
