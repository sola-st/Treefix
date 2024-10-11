# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees.py
"""Transform function call to the compiled counterparts.

  Args:
    node: AST
    ctx: EntityContext
  Returns:
    A tuple (node, new_names):
        node: The transformed AST
        new_names: set(string), containing any newly-generated names
  """
node = qual_names.resolve(node)

node = CallTreeTransformer(ctx).visit(node)
exit(node)
