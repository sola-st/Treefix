from typing import Dict, Tuple # pragma: no cover
from dataclasses import dataclass # pragma: no cover
class Err: pass # pragma: no cover

line = type('Mock', (object,), {})() # pragma: no cover
line.leaves = ['a', 'b', 'c', 'd'] # pragma: no cover
line.clone = lambda: type('MockLine', (object,), {'append': lambda self, leaf, preformatted=False: None})() # pragma: no cover
line.comments_after = lambda leaf: [] # pragma: no cover
is_valid_index_factory = lambda ll: lambda idx: 0 <= idx < len(ll) # pragma: no cover
Leaf = str # pragma: no cover
string_indices = [0, 2] # pragma: no cover
self = type('MockSelf', (object,), {'_validate_msg': lambda self, line, idx: Ok('valid'), '_merge_one_string_group': lambda self, ll, idx, is_valid: (1, ll[idx])})() # pragma: no cover
append_leaves = lambda new_line, old_line, leaves: [new_line.append(leaf) for leaf in leaves] # pragma: no cover

from typing import Dict, Tuple, Any # pragma: no cover
from dataclasses import dataclass, field # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    value: str # pragma: no cover
 # pragma: no cover
@dataclass # pragma: no cover
class Line: # pragma: no cover
    leaves: list = field(default_factory=list) # pragma: no cover
 # pragma: no cover
    def clone(self) -> 'Line': # pragma: no cover
        return Line(self.leaves.copy()) # pragma: no cover
 # pragma: no cover
    def comments_after(self, leaf) -> list: # pragma: no cover
        return [] # pragma: no cover
 # pragma: no cover
    def append(self, leaf: Any, preformatted: bool = False): # pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
 # pragma: no cover
line = Line([Leaf('a'), Leaf('b'), Leaf('c')]) # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(LL): # pragma: no cover
    return lambda idx: 0 <= idx < len(LL) # pragma: no cover
 # pragma: no cover
string_indices = [0, 2] # pragma: no cover
 # pragma: no cover
class Err: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class TErr(Err): # pragma: no cover
    def __init__(self, message): # pragma: no cover
        self.message = message # pragma: no cover
 # pragma: no cover
class Ok: # pragma: no cover
    def __init__(self, result): # pragma: no cover
        self.result = result # pragma: no cover
 # pragma: no cover
def append_leaves(new_line, line, leaves): # pragma: no cover
    new_line.leaves.extend(leaves) # pragma: no cover
 # pragma: no cover
class SelfMock: # pragma: no cover
    def _validate_msg(self, line, string_idx): # pragma: no cover
        return Ok('Valid') # pragma: no cover
 # pragma: no cover
    def _merge_one_string_group(self, LL, string_idx, is_valid_index): # pragma: no cover
        return 1, Leaf(f'merged_{LL[string_idx].value}') # pragma: no cover
 # pragma: no cover
self = SelfMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Merges string groups (i.e. set of adjacent strings).

        Each index from `string_indices` designates one string group's first
        leaf in `line.leaves`.

        Returns:
            Ok(new_line), if ALL of the validation checks found in
            _validate_msg(...) pass.
                OR
            Err(CannotTransform), otherwise.
        """
LL = line.leaves
_l_(17314)

is_valid_index = is_valid_index_factory(LL)
_l_(17315)

# A dict of {string_idx: tuple[num_of_strings, string_leaf]}.
merged_string_idx_dict: Dict[int, Tuple[int, Leaf]] = {}
_l_(17316)
for string_idx in string_indices:
    _l_(17321)

    vresult = self._validate_msg(line, string_idx)
    _l_(17317)
    if isinstance(vresult, Err):
        _l_(17319)

        continue
        _l_(17318)
    merged_string_idx_dict[string_idx] = self._merge_one_string_group(
        LL, string_idx, is_valid_index
    )
    _l_(17320)

if not merged_string_idx_dict:
    _l_(17323)

    aux = TErr("No string group is merged")
    _l_(17322)
    exit(aux)

# Build the final line ('new_line') that this method will later return.
new_line = line.clone()
_l_(17324)
previous_merged_string_idx = -1
_l_(17325)
previous_merged_num_of_strings = -1
_l_(17326)
for i, leaf in enumerate(LL):
    _l_(17336)

    if i in merged_string_idx_dict:
        _l_(17330)

        previous_merged_string_idx = i
        _l_(17327)
        previous_merged_num_of_strings, string_leaf = merged_string_idx_dict[i]
        _l_(17328)
        new_line.append(string_leaf)
        _l_(17329)

    if (
        previous_merged_string_idx
        <= i
        < previous_merged_string_idx + previous_merged_num_of_strings
    ):
        _l_(17334)

        for comment_leaf in line.comments_after(LL[i]):
            _l_(17332)

            new_line.append(comment_leaf, preformatted=True)
            _l_(17331)
        continue
        _l_(17333)

    append_leaves(new_line, line, [leaf])
    _l_(17335)
aux = Ok(new_line)
_l_(17337)

exit(aux)
