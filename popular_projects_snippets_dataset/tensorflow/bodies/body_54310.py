# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
a = constant_op.constant(1)
with ops.control_dependencies([a]):
    b = constant_op.constant(2)
c = constant_op.constant(3)
d = constant_op.constant(4)
e = constant_op.constant(5)
with ops.control_dependencies([a, c]):
    f = d + e

self.assertEqual(a.op.control_inputs, [])
self.assertEqual(b.op.control_inputs, [a.op])
self.assertEqual(f.op.control_inputs, [a.op, c.op])

a.op._remove_all_control_inputs()  # pylint: disable=protected-access
self.assertEqual(a.op.control_inputs, [])

b.op._remove_all_control_inputs()  # pylint: disable=protected-access
self.assertEqual(b.op.control_inputs, [])

f.op._remove_all_control_inputs()  # pylint: disable=protected-access
self.assertEqual(f.op.control_inputs, [])
self.assertEqual(list(f.op.inputs), [d, e])
