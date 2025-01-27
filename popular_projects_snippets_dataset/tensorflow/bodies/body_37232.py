# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(use_gpu=test.is_gpu_available()) as sess:
    var_qint = gen_state_ops.variable(
        shape=[1], dtype=dtypes.qint8, name="v", container="", shared_name="")
    assign_op = state_ops.assign(
        var_qint, constant_op.constant(np.array([42]), dtypes.qint8))
    self.evaluate(assign_op)

    cond = constant_op.constant(True, dtypes.bool)
    v_f, v_t = control_flow_ops.ref_switch(var_qint, cond)
    result = control_flow_ops.ref_merge([v_f, v_t])
    self.evaluate(result)
