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
