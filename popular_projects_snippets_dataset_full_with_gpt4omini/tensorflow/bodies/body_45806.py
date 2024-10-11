# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
"""Basic pattern matcher for AST.

  The pattern may contain wildcards represented by the symbol '_'. A node
  matches a pattern if for every node in the tree, either there is a node of
  the same type in pattern, or a Name node with id='_'.

  Args:
    node: ast.AST
    pattern: ast.AST
  Returns:
    bool
  """
if isinstance(pattern, str):
    pattern = parser.parse_str(pattern)

matcher = PatternMatcher(pattern)
matcher.visit(node)
exit(matcher.matches)
