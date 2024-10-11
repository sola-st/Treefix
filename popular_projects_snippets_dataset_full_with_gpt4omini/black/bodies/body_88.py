# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
            Side Effects:
                If @line starts with a string operator and this is the first
                line we are constructing, this function appends the string
                operator to @new_line and replaces the old string operator leaf
                in the node structure. Otherwise this function does nothing.
            """
maybe_prefix_leaves = string_op_leaves if first_string_line else []
_l_(5810)
for i, prefix_leaf in enumerate(maybe_prefix_leaves):
    _l_(5813)

    replace_child(LL[i], prefix_leaf)
    _l_(5811)
    new_line.append(prefix_leaf)
    _l_(5812)
