# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
a = _apply_op(g, "FloatOutput", [], [dtypes.float32])
with g.control_dependencies([a]):
    b = _apply_op(g, "Identity", [a], [dtypes.float32])

self.assertEqual(b.op.control_inputs, [])
