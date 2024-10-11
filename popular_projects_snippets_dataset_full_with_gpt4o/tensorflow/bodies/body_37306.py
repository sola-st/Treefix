# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
for dtype in self.valid_dtypes:
    x = np.arange(1, 6).reshape([5]).astype(dtype)
    for axis_dtype in [dtypes.int64, dtypes.int32]:
        with self.cached_session():
            axis = constant_op.constant(0, axis_dtype)
            tf_out = math_ops.cumprod(x, axis).eval()
