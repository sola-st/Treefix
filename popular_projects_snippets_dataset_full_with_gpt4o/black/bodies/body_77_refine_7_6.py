from typing import List # pragma: no cover
from dataclasses import dataclass # pragma: no cover
from typing import Any # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
@dataclass # pragma: no cover
class Line: # pragma: no cover
    leaves: List[Leaf] # pragma: no cover
    def comments_after(self, leaf: Leaf) -> bool: # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
line = Line(leaves=[Leaf(), Leaf(), Leaf()]) # pragma: no cover
string_indices = [0, 2] # pragma: no cover
 # pragma: no cover
class StringParser: # pragma: no cover
    def parse(self, leaves: List[Leaf], string_idx: int) -> int: # pragma: no cover
        return string_idx + 1 # pragma: no cover
 # pragma: no cover
Ok = lambda x: 'Ok:' + str(x) # pragma: no cover
Err = lambda x: 'Err:' + str(x) # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def _transform_to_new_line(self, line: Line, indices: List[int]) -> Any: # pragma: no cover
        return 'transformed_line' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

from typing import List # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    value: str # pragma: no cover
 # pragma: no cover
@dataclass # pragma: no cover
class Line: # pragma: no cover
    leaves: List[Leaf] # pragma: no cover
    def comments_after(self, leaf: Leaf) -> bool: # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
line = Line(leaves=[Leaf('('), Leaf('string'), Leaf(')'), Leaf('('), Leaf('string'), Leaf(')')]) # pragma: no cover
string_indices = [1, 4] # pragma: no cover
 # pragma: no cover
class StringParser: # pragma: no cover
    def parse(self, leaves: List[Leaf], string_idx: int) -> int: # pragma: no cover
        # Mock parser to find a corresponding closing parenthesis # pragma: no cover
        open_count = 0 # pragma: no cover
        for i in range(string_idx, len(leaves)): # pragma: no cover
            if leaves[i].value == '(': # pragma: no cover
                open_count += 1 # pragma: no cover
            elif leaves[i].value == ')': # pragma: no cover
                open_count -= 1 # pragma: no cover
                if open_count == 0: # pragma: no cover
                    return i # pragma: no cover
        return -1 # pragma: no cover
 # pragma: no cover
Ok = lambda x: 'Ok: ' + str(x) # pragma: no cover
Err = lambda x: 'Err: ' + str(x) # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def _transform_to_new_line(self, line: Line, indices: List[int]) -> str: # pragma: no cover
        return 'transformed_line' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

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
