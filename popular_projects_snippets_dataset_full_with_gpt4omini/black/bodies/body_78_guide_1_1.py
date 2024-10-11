import token # pragma: no cover
from typing import List # pragma: no cover

class Leaf:  # Mock class to represent a leaf node # pragma: no cover
    def __init__(self, type, value): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
    def remove(self): # pragma: no cover
        pass  # Simulates removal from the tree # pragma: no cover
 # pragma: no cover
class Line:  # Mock class to represent a line in a parse tree # pragma: no cover
    def __init__(self): # pragma: no cover
        self.leaves = [] # pragma: no cover
        self.comments = [] # pragma: no cover
    def clone(self): # pragma: no cover
        new_line = Line() # pragma: no cover
        new_line.comments = self.comments.copy() # pragma: no cover
        return new_line # pragma: no cover
 # pragma: no cover
def append_leaves(new_line, original_line, leaves): # pragma: no cover
    new_line.leaves.extend(leaves)  # Simulates appending leaves # pragma: no cover
 # pragma: no cover
def replace_child(original_leaf, new_leaf): # pragma: no cover
    pass  # Mock method to simulate replacing a leaf # pragma: no cover
 # pragma: no cover
line = Line() # pragma: no cover
line.leaves = [Leaf(token.STRING, 'inner'), Leaf(token.RPAR, ')'), Leaf(token.STRING, 'outer'), Leaf(token.STRING, 'items')] # pragma: no cover
line.comments = [] # pragma: no cover
string_and_rpar_indices = [0, 2]  # Indices of the string and right parenthesis # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
LL = line.leaves
_l_(3845)

new_line = line.clone()
_l_(3846)
new_line.comments = line.comments.copy()
_l_(3847)

previous_idx = -1
_l_(3848)
# We need to sort the indices, since string_idx and its matching
# rpar_idx may not come in order, e.g. in
# `("outer" % ("inner".join(items)))`, the "inner" string's
# string_idx is smaller than "outer" string's rpar_idx.
for idx in sorted(string_and_rpar_indices):
    _l_(3859)

    leaf = LL[idx]
    _l_(3849)
    lpar_or_rpar_idx = idx - 1 if leaf.type == token.STRING else idx
    _l_(3850)
    append_leaves(new_line, line, LL[previous_idx + 1 : lpar_or_rpar_idx])
    _l_(3851)
    if leaf.type == token.STRING:
        _l_(3857)

        string_leaf = Leaf(token.STRING, LL[idx].value)
        _l_(3852)
        LL[lpar_or_rpar_idx].remove()  # Remove lpar.
        _l_(3853)  # Remove lpar.
        replace_child(LL[idx], string_leaf)
        _l_(3854)
        new_line.append(string_leaf)
        _l_(3855)
    else:
        LL[lpar_or_rpar_idx].remove()  # This is a rpar.
        _l_(3856)  # This is a rpar.

    previous_idx = idx
    _l_(3858)

# Append the leaves after the last idx:
append_leaves(new_line, line, LL[idx + 1 :])
_l_(3860)
aux = new_line
_l_(3861)

exit(aux)
