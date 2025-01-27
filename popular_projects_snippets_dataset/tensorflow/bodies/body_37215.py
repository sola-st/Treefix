# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variables.Variable(0)
    c = ops.convert_to_tensor(0)
    one = ops.convert_to_tensor(1)
    two = ops.convert_to_tensor(2)
    p = math_ops.greater_equal(c, 1)

    def a():
        exit(state_ops.assign(v, one))

    def b():
        exit(state_ops.assign(v, two))

    i = control_flow_ops.cond(p, a, b)
    self.assertTrue(isinstance(i, ops.Tensor))
    self.evaluate(variables.global_variables_initializer())

    self.assertEqual(0, self.evaluate(v))

    # True case: c = 2 is >= 1, v is set to 1.
    self.assertEqual(1, i.eval(feed_dict={c.name: 2}))
    self.assertEqual(1, self.evaluate(v))

    # False case: c = 0 is not >= 1, v is set to 2.
    self.assertEqual(2, i.eval(feed_dict={c.name: 0}))
    self.assertEqual(2, self.evaluate(v))
