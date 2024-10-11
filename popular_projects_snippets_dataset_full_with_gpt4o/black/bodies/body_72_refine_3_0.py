from typing import Dict, Tuple # pragma: no cover
from dataclasses import dataclass # pragma: no cover
from typing import Union # pragma: no cover

@dataclass# pragma: no cover
class Leaf:# pragma: no cover
    content: str# pragma: no cover
 # pragma: no cover
line = type('Mock', (object,), {'leaves': [Leaf(content='a'), Leaf(content='b'), Leaf(content='c')], 'clone': lambda self: type('Mock', (object,), {'append': lambda self, leaf, preformatted=False: None})(), 'comments_after': lambda self, leaf: []}) # pragma: no cover
def is_valid_index_factory(LL):# pragma: no cover
    return lambda i: 0 <= i < len(LL)# pragma: no cover
 # pragma: no cover
string_indices = [0, 1, 2] # pragma: no cover
self = type('Mock', (object,), {'_validate_msg': lambda self, line, string_idx: type('Err', (object,), {})() if string_idx % 2 != 0 else None, '_merge_one_string_group': lambda self, LL, string_idx, is_valid_index: (1, Leaf(content=str(string_idx)))})() # pragma: no cover
Err = type('Err', (object,), {}) # pragma: no cover
TErr = lambda msg: type('TErr', (object,), {'msg': msg}) # pragma: no cover
append_leaves = lambda new_line, line, leaves: None # pragma: no cover
Ok = lambda new_line: type('Ok', (object,), {'new_line': new_line}) # pragma: no cover

from typing import Dict, Tuple # pragma: no cover
from dataclasses import dataclass, field # pragma: no cover
from typing import List, Union # pragma: no cover

@dataclass # pragma: no cover
class Leaf: # pragma: no cover
    content: str # pragma: no cover
 # pragma: no cover
@dataclass # pragma: no cover
class Line: # pragma: no cover
    leaves: List[Leaf] = field(default_factory=list) # pragma: no cover
 # pragma: no cover
    def clone(self) -> 'Line': # pragma: no cover
        return Line(self.leaves.copy()) # pragma: no cover
 # pragma: no cover
    def comments_after(self, leaf) -> List[Leaf]: # pragma: no cover
        return []  # Stub implementation, no comments in this example # pragma: no cover
 # pragma: no cover
    def append(self, leaf: Leaf, preformatted: bool = False): # pragma: no cover
        self.leaves.append(leaf) # pragma: no cover
 # pragma: no cover
line = Line([Leaf('string1'), Leaf('string2'), Leaf('string3')]) # pragma: no cover
 # pragma: no cover
def is_valid_index_factory(LL: List[Leaf]): # pragma: no cover
    def is_valid_index(index: int) -> bool: # pragma: no cover
        return 0 <= index < len(LL) # pragma: no cover
    return is_valid_index # pragma: no cover
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
def append_leaves(new_line: Line, line: Line, leaves: List[Leaf]): # pragma: no cover
    for leaf in leaves: # pragma: no cover
        new_line.append(leaf) # pragma: no cover
 # pragma: no cover
class SelfMock: # pragma: no cover
    def _validate_msg(self, line: Line, string_idx: int) -> Union[None, Err]: # pragma: no cover
        return None  # Assume validation always passes # pragma: no cover
 # pragma: no cover
    def _merge_one_string_group(self, LL: List[Leaf], string_idx: int, is_valid_index: callable) -> Tuple[int, Leaf]: # pragma: no cover
        return 1, Leaf(f'merged_{LL[string_idx].content}') # pragma: no cover
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
