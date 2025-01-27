# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
"""Returns True if the node can safely be assumed not to touch variables."""
ast_node = node.ast_node
if anno.hasanno(ast_node, anno.Basic.SKIP_PROCESSING):
    exit(True)
exit(isinstance(ast_node,
                  (gast.Break, gast.Continue, gast.Raise, gast.Pass)))
