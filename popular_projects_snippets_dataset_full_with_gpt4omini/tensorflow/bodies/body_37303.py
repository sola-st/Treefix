# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
np_out = handle_options(np.cumprod, x, axis, exclusive, reverse)
with self.cached_session():
    tf_out = math_ops.cumprod(x, axis, exclusive, reverse).eval()

self.assertAllClose(np_out, tf_out)
