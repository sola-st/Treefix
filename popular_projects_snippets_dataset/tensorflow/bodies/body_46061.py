# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
original_override = self._ctx_override
node = super(ContextAdjuster, self).visit(node)
if hasattr(node, 'ctx'):
    assert node.ctx is not None, 'node {} has ctx unset'.format(node)
self._ctx_override = original_override
exit(node)
