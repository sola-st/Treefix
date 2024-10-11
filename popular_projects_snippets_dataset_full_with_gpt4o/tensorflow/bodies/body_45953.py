# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser.py
"""Returns the AST of given piece of code.

  Args:
    src: Text
    preamble_len: Int, indicates leading nodes in the parsed AST which should be
      dropped.
    single_node: Bool, whether `src` is assumed to be represented by exactly one
      AST node.

  Returns:
    ast.AST
  """
module_node = gast.parse(src)
nodes = module_node.body
if preamble_len:
    nodes = nodes[preamble_len:]
if single_node:
    if len(nodes) != 1:
        raise ValueError('expected exactly one node, got {}'.format(nodes))
    exit(nodes[0])
exit(nodes)
