from typing import List # pragma: no cover
from copy import deepcopy # pragma: no cover
import token # pragma: no cover

line = type('Mock', (object,), {'leaves': [], 'clone': lambda self: deepcopy(self), 'comments': []})() # pragma: no cover
string_and_rpar_indices = [0, 2, 4] # pragma: no cover
def append_leaves(new_line, line, leaves): pass # pragma: no cover
Leaf = type('Leaf', (object,), {'__init__': lambda self, type_, value: setattr(self, 'value', value) or setattr(self, 'type', type_)} ) # pragma: no cover
def replace_child(old, new): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(15367)

new_line = line.clone()
_l_(15368)
new_line.comments = line.comments.copy()
_l_(15369)

previous_idx = -1
_l_(15370)
# We need to sort the indices, since string_idx and its matching
# rpar_idx may not come in order, e.g. in
# `("outer" % ("inner".join(items)))`, the "inner" string's
# string_idx is smaller than "outer" string's rpar_idx.
for idx in sorted(string_and_rpar_indices):
    _l_(15381)

    leaf = LL[idx]
    _l_(15371)
    lpar_or_rpar_idx = idx - 1 if leaf.type == token.STRING else idx
    _l_(15372)
    append_leaves(new_line, line, LL[previous_idx + 1 : lpar_or_rpar_idx])
    _l_(15373)
    if leaf.type == token.STRING:
        _l_(15379)

        string_leaf = Leaf(token.STRING, LL[idx].value)
        _l_(15374)
        LL[lpar_or_rpar_idx].remove()  # Remove lpar.
        _l_(15375)  # Remove lpar.
        replace_child(LL[idx], string_leaf)
        _l_(15376)
        new_line.append(string_leaf)
        _l_(15377)
    else:
        LL[lpar_or_rpar_idx].remove()  # This is a rpar.
        _l_(15378)  # This is a rpar.

    previous_idx = idx
    _l_(15380)

# Append the leaves after the last idx:
append_leaves(new_line, line, LL[idx + 1 :])
_l_(15382)
aux = new_line
_l_(15383)

exit(aux)
