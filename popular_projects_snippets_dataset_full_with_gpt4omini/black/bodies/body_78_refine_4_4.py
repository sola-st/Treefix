from typing import List, Dict # pragma: no cover

string_and_rpar_indices = [0, 2, 1] # pragma: no cover
def append_leaves(new_line, line, leaves): new_line.leaves.extend(leaves) # pragma: no cover

from typing import List # pragma: no cover

class MockToken:# pragma: no cover
    STRING = 'STRING' # pragma: no cover
class MockLeaf:# pragma: no cover
    def __init__(self, type, value=''):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
    def remove(self):# pragma: no cover
        pass # pragma: no cover
def append_leaves(new_line, line, leaves):# pragma: no cover
    new_line.leaves.extend(leaves) # pragma: no cover
def replace_child(old_leaf, new_leaf):# pragma: no cover
    pass # pragma: no cover
LL = [MockLeaf(MockToken.STRING, 'inner'), MockLeaf(MockToken.STRING, 'outer')] # pragma: no cover
class MockLine:# pragma: no cover
    def __init__(self, leaves, comments):# pragma: no cover
        self.leaves = leaves# pragma: no cover
        self.comments = comments# pragma: no cover
    def clone(self):# pragma: no cover
        return MockLine(self.leaves.copy(), self.comments.copy()) # pragma: no cover
line = MockLine(LL, comments=['initial comment']) # pragma: no cover
string_and_rpar_indices = [0, 1] # pragma: no cover

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
