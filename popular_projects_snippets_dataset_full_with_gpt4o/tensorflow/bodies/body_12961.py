# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
i = constant_op.constant(0)
c = control_flow_ops.Assert(i < 10, [i, [10], [i + 1]])
self.evaluate(c)

i = constant_op.constant(10)
c = control_flow_ops.Assert(i < 10, [i, [10], [i + 1]])
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(c)
