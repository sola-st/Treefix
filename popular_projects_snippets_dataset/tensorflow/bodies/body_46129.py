# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Grows the graph by adding an exit node.

    This node becomes an exit for the current section.

    Args:
      ast_node: ast.AST
      section_id: Hashable, the node for which ast_node should be considered to
        be an exit node
      guards: Tuple[ast.AST, ...], the finally sections that guard ast_node

    Returns:
      Node
    """
node = self._add_jump_node(ast_node, guards)
self.exits[section_id].add(node)
exit(node)
