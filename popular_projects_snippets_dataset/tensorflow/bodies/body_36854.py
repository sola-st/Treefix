# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v1 = variables.Variable([7])

    age = constant_op.constant(3)
    pred = math_ops.greater(age, 4)
    fn1 = lambda: age
    fn2 = lambda: v1
    r = control_flow_ops.cond(pred, fn1, fn2)

    self.evaluate(variables.global_variables_initializer())
    result = self.evaluate(r)
    self.assertAllEqual(np.array([7]), result)
