# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(force_gpu=test.is_gpu_available()) as sess:
    constant_uint64 = constant_op.constant(np.array([42]), dtypes.uint64)
    cond = constant_op.constant(True, dtypes.bool)
    v_f, v_t = control_flow_ops.switch(constant_uint64, cond)
    result = control_flow_ops.merge([v_f, v_t])
    self.evaluate(result)
