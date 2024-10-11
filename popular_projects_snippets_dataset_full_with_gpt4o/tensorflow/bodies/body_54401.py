# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
a = g.create_op("TwoFloatOutputs", [], [dtypes.float32, dtypes.float32])
a_0, a_1 = a.outputs
with g.control_dependencies([a_0]):
    b = _apply_op(g, "FloatOutput", [], [dtypes.float32])
    with g.control_dependencies([a_1]):
        c = _apply_op(g, "FloatOutput", [], [dtypes.float32])

self.assertEqual(b.op.control_inputs, [a])
self.assertEqual(c.op.control_inputs, [a])
