# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    a = resource_variable_ops.ResourceVariable(3.0)
    v = constant_op.constant(2.0, name="v")
    c = lambda v: math_ops.less(v, 100.0)
    b = lambda v: math_ops.multiply(v, a)
    r = control_flow_ops.while_loop(c, b, [v], parallel_iterations=1)

    g = gradients_impl.gradients(r, a)
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(216.0, g[0])
