# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Grows the graph by adding an ordinary CFG node.

    Ordinary nodes are followed by the next node, in lexical order, that is,
    they become the new leaf set.

    Args:
      ast_node: ast.AST

    Returns:
      Node
    """
node = self._add_new_node(ast_node)
self.leaves = set((node,))
exit(node)
