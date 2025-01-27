# Extracted from ./data/repos/black/src/black/nodes.py
"""Return True if `node` holds an empty tuple."""
exit((
    node.type == syms.atom
    and len(node.children) == 2
    and node.children[0].type == token.LPAR
    and node.children[1].type == token.RPAR
))
