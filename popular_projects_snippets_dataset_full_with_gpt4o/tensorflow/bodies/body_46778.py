# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates_test.py
if hasattr(node, 'ctx'):
    self.test_instance.assertIsInstance(node.ctx, self.expected_ctx)
if self.at_top_level:
    self.at_top_level = False
    self.expected_ctx = gast.Load
exit(super(_CtxChecker, self).visit(node))
