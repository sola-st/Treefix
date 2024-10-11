# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variables.Variable([0.0, 0.0], dtype=dtypes.float32)

    # If is_constant=True, the shape information should be propagated.
    enter_v_constant = gen_control_flow_ops.enter(
        v, "frame1", is_constant=True)
    self.assertEqual(enter_v_constant.shape, [2])

    # Otherwise, the shape should be unknown.
    enter_v_non_constant = gen_control_flow_ops.enter(
        v, "frame2", is_constant=False)
    self.assertEqual(enter_v_non_constant.shape, None)
