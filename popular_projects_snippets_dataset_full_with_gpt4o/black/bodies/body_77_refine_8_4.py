from typing import List # pragma: no cover
from dataclasses import dataclass, field # pragma: no cover

@dataclass# pragma: no cover
class MockLine:# pragma: no cover
    leaves: List[str] = field(default_factory=list)# pragma: no cover
    def comments_after(self, leaf: str) -> bool:# pragma: no cover
        return False# pragma: no cover
# pragma: no cover
line = MockLine(leaves=['leaf1', 'leaf2', 'leaf3']) # pragma: no cover
string_indices: List[int] = [0, 1, 2] # pragma: no cover
class StringParser:# pragma: no cover
    def parse(self, leaves: List[str], idx: int) -> int:# pragma: no cover
        return idx + 1 # pragma: no cover
class Ok:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value # pragma: no cover
class Err:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value # pragma: no cover
class CannotTransform(Exception):# pragma: no cover
    def __init__(self, message):# pragma: no cover
        super().__init__(message) # pragma: no cover
class MockSelf:# pragma: no cover
    def _transform_to_new_line(self, line, indices):# pragma: no cover
        return 'transformed'# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover

from typing import List # pragma: no cover

line = type('MockLine', (object,), { # pragma: no cover
    'leaves': ['(', 'string1', ')', '(', 'string2', ')', 'string3', ')'], # pragma: no cover
    'comments_after': lambda self, leaf: False # pragma: no cover
})() # pragma: no cover
string_indices = [1, 4] # pragma: no cover
class StringParser: # pragma: no cover
    def parse(self, leaves: List[str], string_idx: int) -> int: # pragma: no cover
        # Return the next parenthesis index for simplicity # pragma: no cover
        for i in range(string_idx, len(leaves)): # pragma: no cover
            if leaves[i] == ')': # pragma: no cover
                return i # pragma: no cover
        return len(leaves) - 1 # pragma: no cover
Ok = lambda x: x # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    '_transform_to_new_line': lambda self, line, indices: 'Transformed line' # pragma: no cover
})() # pragma: no cover
Err = lambda x: x # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover

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
