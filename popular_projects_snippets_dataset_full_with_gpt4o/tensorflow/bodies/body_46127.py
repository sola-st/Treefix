# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Grows the graph by adding a jump node.

    Jump nodes are added to the current leaf set, and the leaf set becomes
    empty. If the jump node is the last in a cond section, then it may be added
    back to the leaf set by a separate mechanism.

    Args:
      ast_node: ast.AST
      guards: Tuple[ast.AST, ...], the finally sections active for this node

    Returns:
      Node
    """
node = self._add_new_node(ast_node)
self.leaves = set()
# The guards themselves may not yet be complete, and will be wired later.
self.finally_sections[node] = guards
exit(node)
