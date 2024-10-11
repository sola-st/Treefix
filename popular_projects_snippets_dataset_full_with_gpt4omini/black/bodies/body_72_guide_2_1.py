from typing import Dict, Tuple, List # pragma: no cover
class Err: pass # pragma: no cover

class Err: pass # pragma: no cover
string_indices = [0, 1, 2] # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_validate_msg': lambda line, idx: Err() if idx == 1 else Ok(None), # pragma: no cover
    '_merge_one_string_group': lambda self, LL, idx, is_valid_index: (1, Leaf()) # pragma: no cover
})() # pragma: no cover
is_valid_index_factory = lambda LL: lambda idx: 0 <= idx < len(LL) # pragma: no cover

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
