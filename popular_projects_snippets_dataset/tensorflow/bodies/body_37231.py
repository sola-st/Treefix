# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(force_gpu=test.is_gpu_available()) as sess:
    constant_qint = constant_op.constant(np.array([42]), dtypes.qint8)
    cond = constant_op.constant(True, dtypes.bool)
    v_f, v_t = control_flow_ops.switch(constant_qint, cond)
    result = control_flow_ops.merge([v_f, v_t])
    self.evaluate(result)
