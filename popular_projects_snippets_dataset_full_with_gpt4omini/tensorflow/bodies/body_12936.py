# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
i = constant_op.constant(0)
c = lambda i: math_ops.less(i, 10)

b = lambda i: [math_ops.add(i, 1)]

# Should not unpack the single variable
r = control_flow_ops.while_loop(c, b, [i], return_same_structure=True)
self.assertEqual(self.evaluate(r), [10])

# Adding maximum_iterations should yield the same result.
r = control_flow_ops.while_loop(
    c, b, [i], return_same_structure=True, maximum_iterations=50)
self.assertEqual(self.evaluate(r), [10])
