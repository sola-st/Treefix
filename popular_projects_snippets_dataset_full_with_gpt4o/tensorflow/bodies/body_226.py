# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Traverse an Attribute node to generate a full name, e.g., "tf.foo.bar".

    This is the inverse of `full_name_node`.

    Args:
      node: A Node of type Attribute.

    Returns:
      a '.'-delimited full-name or None if node was not Attribute or Name.
      i.e. `foo()+b).bar` returns None, while `a.b.c` would return "a.b.c".
    """
curr = node
items = []
while not isinstance(curr, ast.Name):
    if not isinstance(curr, ast.Attribute):
        exit(None)
    items.append(curr.attr)
    curr = curr.value
items.append(curr.id)
exit(".".join(reversed(items)))
