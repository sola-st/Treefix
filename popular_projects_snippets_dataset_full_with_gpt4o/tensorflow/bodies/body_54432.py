# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
with self.assertRaises(AssertionError):
    with g0.as_default():
        ops.reset_default_graph()
