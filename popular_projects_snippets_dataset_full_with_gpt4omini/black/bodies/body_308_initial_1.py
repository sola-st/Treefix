from collections import namedtuple # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, token, value):# pragma: no cover
        self.token = token# pragma: no cover
        self.value = value # pragma: no cover
class Token:# pragma: no cover
    LPAR = 'LPAR'# pragma: no cover
    RPAR = 'RPAR' # pragma: no cover
visible = True # pragma: no cover
class Child:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.prefix = 'child_prefix'# pragma: no cover
    def remove(self):# pragma: no cover
        return 1 # pragma: no cover
class Node:# pragma: no cover
    def __init__(self, symbol, children):# pragma: no cover
        self.symbol = symbol# pragma: no cover
        self.children = children# pragma: no cover
    def insert_child(self, index, child):# pragma: no cover
        self.children.insert(index, child) # pragma: no cover
class Syms:# pragma: no cover
    atom = 'atom' # pragma: no cover
class Parent:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.children = []# pragma: no cover
    def insert_child(self, index, child):# pragma: no cover
        self.children.insert(index, child) # pragma: no cover
token = Token() # pragma: no cover
child = Child() # pragma: no cover
syms = Syms() # pragma: no cover
parent = Parent() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Wrap `child` in parentheses.

    This replaces `child` with an atom holding the parentheses and the old
    child.  That requires moving the prefix.

    If `visible` is False, the leaves will be valueless (and thus invisible).
    """
lpar = Leaf(token.LPAR, "(" if visible else "")
_l_(4110)
rpar = Leaf(token.RPAR, ")" if visible else "")
_l_(4111)
prefix = child.prefix
_l_(4112)
child.prefix = ""
_l_(4113)
index = child.remove() or 0
_l_(4114)
new_child = Node(syms.atom, [lpar, child, rpar])
_l_(4115)
new_child.prefix = prefix
_l_(4116)
parent.insert_child(index, new_child)
_l_(4117)
