# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    v = gen_state_ops.variable(
        shape=[1],
        dtype=dtypes.float32,
        name="v",
        container="",
        shared_name="")
    inited = state_ops.is_variable_initialized(v)
    v_f, v_t = control_flow_ops.ref_switch(v, inited)
    # Both v_f and v_t are uninitialized references. However, an actual use
    # of the reference in the 'true' branch in the 'tf.identity' op will
    # not 'fire' when v is uninitialized, so this is a valid construction.
    # This test tests that ref_identity allows uninitialized ref as input
    # so that this construction is allowed.
    v_f_op = gen_array_ops.ref_identity(v_f)
    v_t_op = gen_array_ops.ref_identity(v_t)
    with ops.control_dependencies([v_f_op]):
        assign_v = state_ops.assign(v, [1.0])
    with ops.control_dependencies([v_t_op]):
        orig_v = array_ops.identity(v)
    merged_op = control_flow_ops.merge([assign_v, orig_v])
    self.assertAllEqual([1.0], self.evaluate(merged_op.output))
