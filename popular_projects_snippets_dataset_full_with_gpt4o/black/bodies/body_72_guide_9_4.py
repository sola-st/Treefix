from typing import Dict, Tuple, List # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, value: str):# pragma: no cover
        self.value = value# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'Leaf(value={self.value})'# pragma: no cover
    def __eq__(self, other):# pragma: no cover
        return isinstance(other, Leaf) and self.value == other.value# pragma: no cover
    def __hash__(self):# pragma: no cover
        return hash(self.value)# pragma: no cover
 # pragma: no cover
class Line:# pragma: no cover
    def __init__(self, leaves: List[Leaf]):# pragma: no cover
        self.leaves = leaves# pragma: no cover
        self.comments_map = {leaves[1]: [Leaf('comment1')], leaves[2]: [Leaf('comment2')]}# pragma: no cover
    def clone(self):# pragma: no cover
        return Line(self.leaves[:])# pragma: no cover
    def append(self, leaf, preformatted=False):# pragma: no cover
        self.leaves.append(leaf)# pragma: no cover
    def comments_after(self, leaf):# pragma: no cover
        return self.comments_map.get(leaf, [])# pragma: no cover
 # pragma: no cover
class Ok:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'Ok(value={self.value})'# pragma: no cover
 # pragma: no cover
class Err:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'Err(value={self.value})'# pragma: no cover
 # pragma: no cover
class TErr(Exception):# pragma: no cover
    def __init__(self, message):# pragma: no cover
        self.message = message# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'TErr(message={self.message})'# pragma: no cover
 # pragma: no cover
def is_valid_index_factory(leaves: List[Leaf]):# pragma: no cover
    def is_valid_index(index: int):# pragma: no cover
        return 0 <= index < len(leaves)# pragma: no cover
    return is_valid_index# pragma: no cover
 # pragma: no cover
def append_leaves(new_line, line, leaves):# pragma: no cover
    for leaf in leaves:# pragma: no cover
        new_line.append(leaf)# pragma: no cover
 # pragma: no cover
    print('Exiting with:', value)# pragma: no cover
 # pragma: no cover
class MockSelf:# pragma: no cover
    def _validate_msg(self, line: Line, string_idx: int):# pragma: no cover
        return Ok('Valid')# pragma: no cover
    def _merge_one_string_group(self, LL: List[Leaf], string_idx: int, is_valid_index):# pragma: no cover
        return (1, Leaf(f'merged_string_{string_idx}'))# pragma: no cover
 # pragma: no cover
line = Line([Leaf('string1'), Leaf('string2'), Leaf('string3')]) # pragma: no cover
string_indices = [0, 1] # pragma: no cover
self = MockSelf() # pragma: no cover

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
