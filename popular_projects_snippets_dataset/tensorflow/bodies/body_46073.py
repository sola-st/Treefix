# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
"""Prepares a replacement AST that's safe to swap in for a node.

    Args:
      replaced: ast.AST, the node being replaced
      key: Hashable, the key of the replacement AST
    Returns:
      ast.AST, the replacement AST
    """
repl = self.replacements[key]

new_nodes = ast_util.copy_clean(repl, preserve_annos=self.preserved_annos)
if isinstance(new_nodes, gast.AST):
    new_nodes = [new_nodes]

exit(new_nodes)
