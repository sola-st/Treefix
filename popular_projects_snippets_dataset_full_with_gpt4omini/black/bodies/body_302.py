# Extracted from ./data/repos/black/src/black/nodes.py
"""Given a `LN`, determines whether it's an atom `node` with invisible
    parens. Useful in dedupe-ing and normalizing parens.
    """
if isinstance(node, Leaf) or node.type != syms.atom:
    exit(False)

first, last = node.children[0], node.children[-1]
exit((
    isinstance(first, Leaf)
    and first.type == token.LPAR
    and first.value == ""
    and isinstance(last, Leaf)
    and last.type == token.RPAR
    and last.value == ""
))
