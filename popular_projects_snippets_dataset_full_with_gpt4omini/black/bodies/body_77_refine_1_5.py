from typing import List, Any # pragma: no cover
from dataclasses import dataclass # pragma: no cover

class MockLine:# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves# pragma: no cover
    def comments_after(self, leaf):# pragma: no cover
        return False # pragma: no cover
line = MockLine(leaves=['foo', 'bar', '(', 'baz', ')']) # pragma: no cover
string_indices = [2] # pragma: no cover
class StringParser:# pragma: no cover
    def parse(self, leaves, index):# pragma: no cover
        return index + 1 # pragma: no cover
Ok = lambda x: f'Ok: {x}' # pragma: no cover
class MockSelf:# pragma: no cover
    def _transform_to_new_line(self, line, indices):# pragma: no cover
        return f'Transformed line with indices: {indices}'# pragma: no cover
self = MockSelf() # pragma: no cover
class Err:# pragma: no cover
    def __init__(self, msg):# pragma: no cover
        self.msg = msg# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'Err: {self.msg}' # pragma: no cover
class CannotTransform:# pragma: no cover
    def __init__(self, msg):# pragma: no cover
        self.msg = msg# pragma: no cover
    def __repr__(self):# pragma: no cover
        return msg # pragma: no cover

from typing import List, Any # pragma: no cover
from dataclasses import dataclass # pragma: no cover

class MockLine:# pragma: no cover
    def __init__(self, leaves):# pragma: no cover
        self.leaves = leaves# pragma: no cover
    def comments_after(self, leaf):# pragma: no cover
        return False # pragma: no cover
line = MockLine(leaves=['foo', 'bar', '(', 'baz', ')']) # pragma: no cover
string_indices = [2] # pragma: no cover
class StringParser:# pragma: no cover
    def parse(self, leaves, index):# pragma: no cover
        return index + 1 # pragma: no cover
Ok = lambda x: f'Ok: {x}' # pragma: no cover
class MockSelf:# pragma: no cover
    def _transform_to_new_line(self, line, indices):# pragma: no cover
        return f'Transformed line with indices: {indices}'# pragma: no cover
self = MockSelf() # pragma: no cover
class Err:# pragma: no cover
    def __init__(self, msg):# pragma: no cover
        self.msg = msg# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'Err: {self.msg}' # pragma: no cover
class CannotTransform:# pragma: no cover
    def __init__(self, msg):# pragma: no cover
        self.msg = msg# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'CannotTransform: {self.msg}' # pragma: no cover

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
