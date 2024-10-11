from typing import List, Optional # pragma: no cover

class MockNode: pass# pragma: no cover
 # pragma: no cover
node = MockNode()# pragma: no cover
 # pragma: no cover
node.type = 'trailer'# pragma: no cover
 # pragma: no cover
node.children = []# pragma: no cover
 # pragma: no cover
child1 = MockNode()# pragma: no cover
 # pragma: no cover
child1.type = 'DOT'# pragma: no cover
 # pragma: no cover
child2 = MockNode()# pragma: no cover
 # pragma: no cover
child2.type = 'NAME'# pragma: no cover
 # pragma: no cover
node.children.append(child1)# pragma: no cover
 # pragma: no cover
node.children.append(child2)# pragma: no cover
 # pragma: no cover
class MockSymbols: pass# pragma: no cover
 # pragma: no cover
syms = MockSymbols()# pragma: no cover
 # pragma: no cover
syms.trailer = 'trailer'# pragma: no cover
 # pragma: no cover
class MockToken:# pragma: no cover
 # pragma: no cover
    DOT = 'DOT'# pragma: no cover
 # pragma: no cover
    NAME = 'NAME'# pragma: no cover
 # pragma: no cover
    LPAR = 'LPAR'# pragma: no cover
 # pragma: no cover
    RPAR = 'RPAR'# pragma: no cover
 # pragma: no cover
token = MockToken()# pragma: no cover
 # pragma: no cover
last = False# pragma: no cover
 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True iff `node` is a trailer valid in a simple decorator"""
aux = node.type == syms.trailer and (
    (
        len(node.children) == 2
        and node.children[0].type == token.DOT
        and node.children[1].type == token.NAME
    )
    # last trailer can be an argument-less parentheses pair
    or (
        last
        and len(node.children) == 2
        and node.children[0].type == token.LPAR
        and node.children[1].type == token.RPAR
    )
    # last trailer can be arguments
    or (
        last
        and len(node.children) == 3
        and node.children[0].type == token.LPAR
        # and node.children[1].type == syms.argument
        and node.children[2].type == token.RPAR
    )
)
_l_(5181)
exit(aux)
