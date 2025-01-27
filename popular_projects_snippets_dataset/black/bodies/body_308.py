# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Wrap `child` in parentheses.

    This replaces `child` with an atom holding the parentheses and the old
    child.  That requires moving the prefix.

    If `visible` is False, the leaves will be valueless (and thus invisible).
    """
lpar = Leaf(token.LPAR, "(" if visible else "")
_l_(15963)
rpar = Leaf(token.RPAR, ")" if visible else "")
_l_(15964)
prefix = child.prefix
_l_(15965)
child.prefix = ""
_l_(15966)
index = child.remove() or 0
_l_(15967)
new_child = Node(syms.atom, [lpar, child, rpar])
_l_(15968)
new_child.prefix = prefix
_l_(15969)
parent.insert_child(index, new_child)
_l_(15970)
