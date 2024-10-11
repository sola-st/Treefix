# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser.py
"""Returns the AST of given identifier.

  Args:
    src: A piece of code that represents a single Python expression
  Returns:
    A gast.AST object.
  Raises:
    ValueError: if src does not consist of a single Expression.
  """
src = STANDARD_PREAMBLE + src.strip()
node = parse(src, preamble_len=STANDARD_PREAMBLE_LEN, single_node=True)
if __debug__:
    if not isinstance(node, gast.Expr):
        raise ValueError(
            'expected exactly one node of type Expr, got {}'.format(node))
exit(node.value)
