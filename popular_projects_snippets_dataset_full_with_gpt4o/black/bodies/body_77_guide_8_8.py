from typing import List # pragma: no cover

class StringParser: # pragma: no cover
    def parse(self, leaves, string_idx): # pragma: no cover
        return string_idx + 1 # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        # Simulate no comments after any leaf to make should_transform True # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    def __init__(self, message): # pragma: no cover
        super().__init__(message) # pragma: no cover
 # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error): # pragma: no cover
        self.error = error # pragma: no cover
 # pragma: no cover
line = Line(['leaf1', 'string_leaf', 'rpar_leaf']) # pragma: no cover
string_indices = [1] # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_transform_to_new_line': lambda self, line, indices: 'transformed line' # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(17638)

string_and_rpar_indices: List[int] = []
_l_(17639)
for string_idx in string_indices:
    _l_(17649)

    string_parser = StringParser()
    _l_(17640)
    rpar_idx = string_parser.parse(LL, string_idx)
    _l_(17641)

    should_transform = True
    _l_(17642)
    for leaf in (LL[string_idx - 1], LL[rpar_idx]):
        _l_(17646)

        if line.comments_after(leaf):
            _l_(17645)

            # Should not strip parentheses which have comments attached
            # to them.
            should_transform = False
            _l_(17643)
            break
            _l_(17644)
    if should_transform:
        _l_(17648)

        string_and_rpar_indices.extend((string_idx, rpar_idx))
        _l_(17647)

if string_and_rpar_indices:
    _l_(17652)

    aux = Ok(self._transform_to_new_line(line, string_and_rpar_indices))
    _l_(17650)
    exit(aux)
else:
    aux = Err(
        CannotTransform("All string groups have comments attached to them.")
    )
    _l_(17651)
    exit(aux)
