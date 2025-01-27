# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
orig = ops.get_default_graph()
self.assertFalse(ops.has_default_graph())
self._AssertDefault(orig)
g0 = ops.Graph()
self.assertFalse(ops.has_default_graph())
self._AssertDefault(orig)
context_manager_0 = g0.as_default()
self.assertFalse(ops.has_default_graph())
self._AssertDefault(orig)
with context_manager_0 as g0:
    self._AssertDefault(g0)
    with ops.Graph().as_default() as g1:
        self.assertTrue(ops.has_default_graph())
        self._AssertDefault(g1)
    self._AssertDefault(g0)
self._AssertDefault(orig)
self.assertFalse(ops.has_default_graph())
