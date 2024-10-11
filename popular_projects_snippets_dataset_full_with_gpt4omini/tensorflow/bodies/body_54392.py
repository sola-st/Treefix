# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
t1 = _apply_op(g, "FloatOutput", [], [dtypes.float32], name="myop1")
t2 = _apply_op(g, "FloatOutput", [], [dtypes.float32], name="myop2")
self.assertTrue(isinstance(t1, ops.Tensor))
self.assertTrue(isinstance(t2, ops.Tensor))
self.assertTrue(t1 in [t1])
self.assertTrue(t1 not in [t2])
