# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variables.VariableV1(
        np.array([[0.0, 1.0], [10.0, 11.0], [20.0, 21.0]]).astype(np.float32))
    v_at_1 = indexed_slices.IndexedSlices(v, constant_op.constant([1]))
    gather_v_at_1 = array_ops.gather(v_at_1.values, v_at_1.indices)
    v_at_1_after_init = control_flow_ops.with_dependencies([v.initializer],
                                                           v_at_1)
    gather_v_at_1_after_init = array_ops.gather(v_at_1_after_init.values,
                                                v_at_1_after_init.indices)

    # Fetching gather_v_at_1 will result in an uninitialized error
    with self.assertRaisesOpError("Attempting to use uninitialized value"):
        self.evaluate(gather_v_at_1)

    # Getting gather_v_at_1_after_init will work, and initialize v.
    self.assertAllEqual([[10.0, 11.0]],
                        self.evaluate(gather_v_at_1_after_init))

    # Double check that 'v' is initialized
    self.assertAllClose([[0.0, 1.0], [10.0, 11.0], [20.0, 21.0]],
                        self.evaluate(v))
