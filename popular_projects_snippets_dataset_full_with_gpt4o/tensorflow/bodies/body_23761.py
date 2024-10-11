# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
a = a.astype(np.float32) if a.dtype == float_type else a
b = b.astype(np.float32) if b.dtype == float_type else b
exit(np.testing.assert_allclose(a, b, **kwargs))
