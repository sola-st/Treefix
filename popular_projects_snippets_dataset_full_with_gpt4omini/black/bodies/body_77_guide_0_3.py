from typing import List # pragma: no cover
class Err: pass # pragma: no cover
class Ok: pass # pragma: no cover
class CannotTransform(Exception): pass # pragma: no cover
class StringParser: pass # pragma: no cover
class Line: pass # pragma: no cover

class MockLine(object): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = ['(', 'example', ')'] # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        return False  # No comments attached to leaves # pragma: no cover
 # pragma: no cover
line = MockLine() # pragma: no cover
string_indices = [0]  # Index of the first string to be parsed # pragma: no cover
LL = line.leaves # pragma: no cover
self = type('MockSelf', (object,), {'_transform_to_new_line': lambda self, line, indices: 'Transformed line'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(5887)

string_and_rpar_indices: List[int] = []
_l_(5888)
for string_idx in string_indices:
    _l_(5898)

    string_parser = StringParser()
    _l_(5889)
    rpar_idx = string_parser.parse(LL, string_idx)
    _l_(5890)

    should_transform = True
    _l_(5891)
    for leaf in (LL[string_idx - 1], LL[rpar_idx]):
        _l_(5895)

        if line.comments_after(leaf):
            _l_(5894)

            # Should not strip parentheses which have comments attached
            # to them.
            should_transform = False
            _l_(5892)
            break
            _l_(5893)
    if should_transform:
        _l_(5897)

        string_and_rpar_indices.extend((string_idx, rpar_idx))
        _l_(5896)

if string_and_rpar_indices:
    _l_(5901)

    aux = Ok(self._transform_to_new_line(line, string_and_rpar_indices))
    _l_(5899)
    exit(aux)
else:
    aux = Err(
        CannotTransform("All string groups have comments attached to them.")
    )
    _l_(5900)
    exit(aux)
