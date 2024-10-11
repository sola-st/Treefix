# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    v = variables.VariableV1(0.0)
    c = constant_op.constant(10)

    # Fetching v directly will result in an uninitialized error
    with self.assertRaisesOpError("Attempting to use uninitialized value"):
        self.evaluate([c, v])

    # Use a control dependency to ensure init_variable is run
    # while asking for c
    real_v = control_flow_ops.with_dependencies(
        name="real_tensor",
        output_tensor=v._ref(),  # pylint: disable=protected-access
        dependencies=[v.initializer])
    c_val, real_v_val = self.evaluate([c, real_v])

# Ensure the result of 'real_c' is the same as 'c'
self.assertAllEqual(10, c_val)

# Ensure that 'v' is initialized
self.assertAllClose(0.0, real_v_val)
