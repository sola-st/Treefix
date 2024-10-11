# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
i = constant_op.constant(0)
c = lambda i: math_ops.less(i, 10)
b = lambda i: (math_ops.add(i, 1),)
r = control_flow_ops.while_loop(c, b, [i])

# Expect a tuple since that is what the body returns.
self.assertEqual(self.evaluate(r), (10,))
