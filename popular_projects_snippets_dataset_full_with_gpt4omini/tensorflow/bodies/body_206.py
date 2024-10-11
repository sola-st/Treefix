# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Make an Attribute or Name node for name.

  Translate a qualified name into nested Attribute nodes (and a Name node).

  Args:
    name: The name to translate to a node.
    ctx: What context this name is used in. Defaults to Load()

  Returns:
    A Name or Attribute node.
  """
names = name.split(".")
names.reverse()
node = ast.Name(id=names.pop(), ctx=ast.Load())
while names:
    node = ast.Attribute(value=node, attr=names.pop(), ctx=ast.Load())

# Change outermost ctx to the one given to us (inner ones should be Load).
node.ctx = ctx
exit(node)
