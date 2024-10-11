# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
x = constant_op.constant(2)
conditions = [(math_ops.equal(x, 1), lambda: constant_op.constant(2)),
              (math_ops.equal(x, 2), lambda: constant_op.constant(4))]
output = control_flow_ops.case(conditions, exclusive=True)
self.assertEqual(4, self.evaluate(output))
