# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
a = constant_op.constant(2.0)
self.assertTrue(g.is_fetchable(a))
g.prevent_fetching(a.op)
self.assertFalse(g.is_fetchable(a))
