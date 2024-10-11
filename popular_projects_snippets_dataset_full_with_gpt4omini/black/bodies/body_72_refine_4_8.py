from typing import Dict, Tuple # pragma: no cover

class Leaf: pass # pragma: no cover
class Line:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [] # pragma: no cover
        self.comments = [] # pragma: no cover
    def clone(self): # pragma: no cover
        new_line = Line() # pragma: no cover
        new_line.leaves = self.leaves.copy() # pragma: no cover
        return new_line # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        return self.comments[self.leaves.index(leaf):] if leaf in self.leaves else [] # pragma: no cover
def is_valid_index_factory(LL): # pragma: no cover
    return lambda idx: 0 <= idx < len(LL) # pragma: no cover
string_indices = [0, 1] # pragma: no cover
line = Line() # pragma: no cover
self = type('MockSelf', (), { '_validate_msg': lambda self, line, idx: Ok(None), '_merge_one_string_group': lambda LL, idx, is_valid_index: (1, Leaf()) })() # pragma: no cover
class Err: pass # pragma: no cover
class Ok:  # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
class TErr:  # pragma: no cover
    def __init__(self, message): # pragma: no cover
        self.message = message # pragma: no cover
def append_leaves(new_line, line, leaves): # pragma: no cover
    new_line.leaves.extend(leaves) # pragma: no cover

from typing import Dict, Tuple # pragma: no cover

class Leaf: pass # pragma: no cover
class Line:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [Leaf() for _ in range(5)] # pragma: no cover
        self.comments = [Leaf() for _ in range(5)] # pragma: no cover
    def clone(self): # pragma: no cover
        new_line = Line() # pragma: no cover
        new_line.leaves = self.leaves.copy() # pragma: no cover
        return new_line # pragma: no cover
    def comments_after(self, leaf): # pragma: no cover
        return self.comments[self.leaves.index(leaf):] if leaf in self.leaves else [] # pragma: no cover
def is_valid_index_factory(LL): # pragma: no cover
    return lambda idx: 0 <= idx < len(LL) # pragma: no cover
string_indices = [0, 1] # pragma: no cover
line = Line() # pragma: no cover
self = type('MockSelf', (), { '_validate_msg': lambda self, line, idx: Ok(None), '_merge_one_string_group': lambda self, LL, idx: (1, LL[idx]) })() # pragma: no cover
class Err: pass # pragma: no cover
class Ok:  # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
class TErr:  # pragma: no cover
    def __init__(self, message): # pragma: no cover
        self.message = message # pragma: no cover
def append_leaves(new_line, line, leaves): # pragma: no cover
    new_line.leaves.extend(leaves) # pragma: no cover

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
_l_(5544)

is_valid_index = is_valid_index_factory(LL)
_l_(5545)

# A dict of {string_idx: tuple[num_of_strings, string_leaf]}.
merged_string_idx_dict: Dict[int, Tuple[int, Leaf]] = {}
_l_(5546)
for string_idx in string_indices:
    _l_(5551)

    vresult = self._validate_msg(line, string_idx)
    _l_(5547)
    if isinstance(vresult, Err):
        _l_(5549)

        continue
        _l_(5548)
    merged_string_idx_dict[string_idx] = self._merge_one_string_group(
        LL, string_idx, is_valid_index
    )
    _l_(5550)

if not merged_string_idx_dict:
    _l_(5553)

    aux = TErr("No string group is merged")
    _l_(5552)
    exit(aux)

# Build the final line ('new_line') that this method will later return.
new_line = line.clone()
_l_(5554)
previous_merged_string_idx = -1
_l_(5555)
previous_merged_num_of_strings = -1
_l_(5556)
for i, leaf in enumerate(LL):
    _l_(5566)

    if i in merged_string_idx_dict:
        _l_(5560)

        previous_merged_string_idx = i
        _l_(5557)
        previous_merged_num_of_strings, string_leaf = merged_string_idx_dict[i]
        _l_(5558)
        new_line.append(string_leaf)
        _l_(5559)

    if (
        previous_merged_string_idx
        <= i
        < previous_merged_string_idx + previous_merged_num_of_strings
    ):
        _l_(5564)

        for comment_leaf in line.comments_after(LL[i]):
            _l_(5562)

            new_line.append(comment_leaf, preformatted=True)
            _l_(5561)
        continue
        _l_(5563)

    append_leaves(new_line, line, [leaf])
    _l_(5565)
aux = Ok(new_line)
_l_(5567)

exit(aux)
