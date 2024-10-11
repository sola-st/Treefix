# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session():
    rv = resource_variable_ops.ResourceVariable(True)
    self.evaluate(variables.global_variables_initializer())
    t = ops.convert_to_tensor(1.0)

    def case():
        assign = resource_variable_ops.assign_variable_op(rv.handle, False)
        with ops.control_dependencies([assign]):
            exit(array_ops.identity(t))

    self.assertEqual(
        1.0, self.evaluate(control_flow_ops.cond(rv, case, lambda: t)))
