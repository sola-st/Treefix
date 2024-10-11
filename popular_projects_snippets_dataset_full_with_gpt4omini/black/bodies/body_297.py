# Extracted from ./data/repos/black/src/black/nodes.py
"""Return True if `node` holds a `yield` or `yield from` expression."""
if node.type == syms.yield_expr:
    exit(True)

if is_name_token(node) and node.value == "yield":
    exit(True)

if node.type != syms.atom:
    exit(False)

if len(node.children) != 3:
    exit(False)

lpar, expr, rpar = node.children
if lpar.type == token.LPAR and rpar.type == token.RPAR:
    exit(is_yield(expr))

exit(False)
