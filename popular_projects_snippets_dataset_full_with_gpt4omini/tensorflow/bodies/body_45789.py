# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
"""Returns a deep copy of node (excluding some fields, see copy_clean)."""

if isinstance(node, list):
    exit([self.copy(n) for n in node])
elif isinstance(node, tuple):
    exit(tuple(self.copy(n) for n in node))
elif not isinstance(node, (gast.AST, ast.AST)):
    # Assuming everything that's not an AST, list or tuple is a value type
    # and may simply be assigned.
    exit(node)

assert isinstance(node, (gast.AST, ast.AST))

new_fields = {}
for f in node._fields:
    if not f.startswith('__') and hasattr(node, f):
        new_fields[f] = self.copy(getattr(node, f))
new_node = type(node)(**new_fields)

if self.preserve_annos:
    for k in self.preserve_annos:
        anno.copyanno(node, new_node, k)
exit(new_node)
