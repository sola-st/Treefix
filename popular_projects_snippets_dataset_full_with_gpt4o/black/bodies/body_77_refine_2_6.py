from typing import List # pragma: no cover
from typing import Any # pragma: no cover

line = type('Mock', (object,), {})() # pragma: no cover
line.leaves = ['(', 'string1', ')', '(', 'string2', ')'] # pragma: no cover
line.comments_after = lambda leaf: False # pragma: no cover
string_indices = [1, 4] # pragma: no cover
class StringParser:# pragma: no cover
    def parse(self, leaves: List[str], string_idx: int) -> int:# pragma: no cover
        # Mock parse method to find corresponding closing parenthesis# pragma: no cover
        for idx, leaf in enumerate(leaves[string_idx:], start=string_idx):# pragma: no cover
            if leaf == ')':# pragma: no cover
                return idx# pragma: no cover
        return -1 # pragma: no cover
Ok = lambda x: x # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    '_transform_to_new_line': lambda self, line, indices: 'transformed_line'# pragma: no cover
})() # pragma: no cover
Err = lambda x: x # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {}) # pragma: no cover

from typing import List # pragma: no cover
from typing import Any # pragma: no cover

line = type('Mock', (object,), {})() # pragma: no cover
line.leaves = ['(', 'string1', ')', '(', 'string2', ')'] # pragma: no cover
line.comments_after = lambda self, leaf: False # pragma: no cover
string_indices = [1, 4] # pragma: no cover
class StringParser:# pragma: no cover
    def parse(self, leaves: List[str], string_idx: int) -> int:# pragma: no cover
        # Mock parse method to find corresponding closing parenthesis# pragma: no cover
        for idx, leaf in enumerate(leaves[string_idx:], start=string_idx):# pragma: no cover
            if leaf == ')':# pragma: no cover
                return idx# pragma: no cover
        return -1 # pragma: no cover
Ok = lambda x: x # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    '_transform_to_new_line': lambda self, line, indices: 'transformed_line'# pragma: no cover
})() # pragma: no cover
Err = type('Err', (object,), {'__init__': lambda self, error: setattr(self, 'error', error)}) # pragma: no cover
CannotTransform = type('CannotTransform', (Exception,), {'__init__': lambda self, message: super(CannotTransform, self).__init__(message)}) # pragma: no cover

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
