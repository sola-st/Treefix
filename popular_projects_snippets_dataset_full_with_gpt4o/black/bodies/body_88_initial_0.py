string_op_leaves = ['+', '-'] # pragma: no cover
first_string_line = True # pragma: no cover
def replace_child(LL_item, prefix_leaf):# pragma: no cover
    pass  # placeholder implementation # pragma: no cover
LL = ['a', 'b', 'c'] # pragma: no cover
new_line = type('Mock', (object,), {'append': lambda self, x: None})() # pragma: no cover

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
_l_(17622)
for i, prefix_leaf in enumerate(maybe_prefix_leaves):
    _l_(17625)

    replace_child(LL[i], prefix_leaf)
    _l_(17623)
    new_line.append(prefix_leaf)
    _l_(17624)
