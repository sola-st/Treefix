# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
i = constant_op.constant(0)
c = lambda i, _: math_ops.less(i, 10)

# Body returns a [tensor, []]
b = lambda i, _: [math_ops.add(i, 1), []]

# Should only return the tensor.
r = control_flow_ops.while_loop(c, b, [i, []])
self.assertEqual(self.evaluate(r), 10)

# Adding maximum_iterations should yield the same result.
r = control_flow_ops.while_loop(c, b, [i, []], maximum_iterations=50)
# Note: this result is still incorrect - it should be just 10.
self.assertEqual(self.evaluate(r), [10, []])
