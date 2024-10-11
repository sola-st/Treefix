# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Returns a name for the output function. Subclasses may override this."""
if isinstance(node, gast.Lambda):
    exit('lam')
elif isinstance(node, gast.FunctionDef):
    exit(node.name)
raise ValueError('Unknown node type {}'.format(node))
