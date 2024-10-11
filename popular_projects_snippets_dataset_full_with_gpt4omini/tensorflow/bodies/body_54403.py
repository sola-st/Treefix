# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
a = _apply_op(g, "FloatOutput", [], [dtypes.float32])
b = _apply_op(g, "FloatOutput", [], [dtypes.float32])
with g.control_dependencies([a]):
    c = _apply_op(g, "Identity", [b], [dtypes.float32])

with g.control_dependencies([b]):
    d = _apply_op(g, "Identity", [b], [dtypes.float32])

# Validate that the monitoring attribute is set to track usage of the
# `control_dependencies(...)` API.
self.assertEqual(c.op.control_inputs, [a.op])
with self.assertRaises(ValueError):
    c.op.get_attr("_has_manual_control_dependencies")
self.assertEqual(a.op.get_attr("_has_manual_control_dependencies"), True)

# Validate that the monitoring attribute is set to track usage of the
# `control_dependencies(...)` API even when the manual control deps actually
# happened to be pruned at runtime.
self.assertEqual(d.op.control_inputs, [])
with self.assertRaises(ValueError):
    d.op.get_attr("_has_manual_control_dependencies")
self.assertEqual(b.op.get_attr("_has_manual_control_dependencies"), True)
