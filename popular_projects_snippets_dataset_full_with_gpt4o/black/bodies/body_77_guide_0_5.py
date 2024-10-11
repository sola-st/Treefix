from typing import List # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class MockStringParser: # pragma: no cover
    def parse(self, leaves, idx): # pragma: no cover
        return idx + 1 # pragma: no cover
 # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, leaves): # pragma: no cover
        self.leaves = leaves # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        # Simulate comments attached to the leaves # pragma: no cover
        return True if leaf == self.leaves[-1] else False # pragma: no cover
    def _transform_to_new_line(self, line, indices): # pragma: no cover
        return 'Transformed' # pragma: no cover
 # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class Err: # pragma: no cover
    def __init__(self, error): # pragma: no cover
        self.error = error # pragma: no cover
 # pragma: no cover
class CannotTransform(Exception): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
line = MockLine(['leaf1', 'leaf2', 'leaf3']) # pragma: no cover
line.leaves = ['leaf1', 'leaf2', 'leaf3'] # pragma: no cover
string_indices = [1] # pragma: no cover
self = type('Mock', (object,), {'_transform_to_new_line': line._transform_to_new_line})() # pragma: no cover

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
