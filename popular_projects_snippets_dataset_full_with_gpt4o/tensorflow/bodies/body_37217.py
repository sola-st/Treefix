# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variables.VariableV1(0.0)
    c1 = constant_op.constant(10)
    c2 = constant_op.constant(20)

    # c1_with_init_v depends on the init op for v
    c1_with_init_v = control_flow_ops.with_dependencies(
        name="c1_with_init_v", output_tensor=c1, dependencies=[v.initializer])
    # c2_with_c1 depends on the value of c1_with_init_v
    c2_with_c1_dep = control_flow_ops.with_dependencies(
        name="c2_with_c1_dep",
        output_tensor=c2,
        dependencies=[c1_with_init_v])

    # Fetching v directly will result in an uninitialized error
    with self.assertRaisesOpError("Attempting to use uninitialized value"):
        self.evaluate(v)

    # Get the value of 'c2_with_c1_dep', which should cause 'v'
    # to be initialized.
    self.assertAllEqual(20, self.evaluate(c2_with_c1_dep))

    # Ensure that 'v' is initialized
    self.assertAllClose(0.0, self.evaluate(v))
