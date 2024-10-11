# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
super(_CtxClearer, self).visit(node)
if hasattr(node, 'ctx'):
    node.ctx = None
exit(node)
