# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/histogram_ops_test.py
hist = histogram_ops.histogram_fixed_width(
    values=constant_op.constant([3e+38, 100], dtype=dtypes.float32),
    value_range=constant_op.constant([-1e+38, 3e+38]),
    nbins=2)
self.assertAllEqual(hist, [1, 1])
