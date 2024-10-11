# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
"""Renames symbols in an AST. Requires qual_names annotations."""
renamer = SymbolRenamer(name_map)
if isinstance(node, list):
    exit([renamer.visit(n) for n in node])
elif isinstance(node, tuple):
    exit(tuple(renamer.visit(n) for n in node))
exit(renamer.visit(node))
