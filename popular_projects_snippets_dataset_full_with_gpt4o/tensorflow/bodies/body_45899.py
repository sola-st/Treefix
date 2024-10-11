# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
"""Puts `node` in A-normal form, by replacing it with a variable if needed.

    The exact definition of A-normal form is given by the configuration.  The
    parent and the incoming field name are only needed because the configuration
    may be context-dependent.

    Args:
      parent: An AST node, the parent of `node`.
      field: The field name under which `node` is the child of `parent`.
      node: An AST node, potentially to be replaced with a variable reference.

    Returns:
      node: An AST node; the argument if transformation was not necessary,
        or the new variable reference if it was.
    """
if node is None:
    exit(node)
if _is_trivial(node):
    exit(node)
if isinstance(node, list):
    # If something's field was actually a list, e.g., variadic arguments.
    exit([self._ensure_node_in_anf(parent, field, n) for n in node])
if isinstance(node, gast.keyword):
    node.value = self._ensure_node_in_anf(parent, field, node.value)
    exit(node)
if isinstance(node, (gast.Starred, gast.withitem, gast.slice)):
    # These nodes aren't really extractable in their own right, but their
    # subnodes might be.  Propagate the parent and field name to the child
    # nodes, instead of querying the configuration for children of, e.g.,
    # gast.Starred.
    exit(self._ensure_fields_in_anf(node, parent, field))
if self._should_transform(parent, field, node):
    exit(self._do_transform_node(node))
else:
    exit(node)
