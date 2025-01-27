# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Grows the graph by adding a reentry node.

    This node causes control flow to go back to the loop section's entry.

    Args:
      ast_node: ast.AST
      section_id: Hashable, the node for which ast_node should be considered to
        be an exit node
      guards: Tuple[ast.AST, ...], the finally sections that guard ast_node
    """
node = self._add_jump_node(ast_node, guards)
self.continues[section_id].add(node)
