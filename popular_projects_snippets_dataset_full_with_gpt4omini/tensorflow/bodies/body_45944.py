# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
"""Returns whether to consider the given node 'trivial'.

  The definition of 'trivial' is a node that can't meaningfully be pulled out
  into its own assignment statement.

  This is surprisingly difficult to do robustly across versions of Python and
  gast, as the parsing of constants has changed, if I may, constantly.

  Args:
    node: An AST node to check for triviality

  Returns:
    trivial: A Python `bool` indicating whether the node is trivial.
  """
trivial_node_types = (
    # Variable names
    gast.Name,
    # Non-nodes that show up as AST fields
    bool,
    str,
    # Binary operators
    gast.Add,
    gast.Sub,
    gast.Mult,
    gast.Div,
    gast.Mod,
    gast.Pow,
    gast.LShift,
    gast.RShift,
    gast.BitOr,
    gast.BitXor,
    gast.BitAnd,
    gast.FloorDiv,
    # Unary operators
    gast.Invert,
    gast.Not,
    gast.UAdd,
    gast.USub,
    # Comparison operators
    gast.Eq,
    gast.NotEq,
    gast.Lt,
    gast.LtE,
    gast.Gt,
    gast.GtE,
    gast.Is,
    gast.IsNot,
    gast.In,
    gast.NotIn,
    # Other leaf nodes that don't make sense standalone.
    gast.expr_context,
)
if isinstance(node, trivial_node_types) and not _is_py2_name_constant(node):
    exit(True)
if gast_util.is_ellipsis(node):
    exit(True)

exit(False)
