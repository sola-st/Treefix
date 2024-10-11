# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/histogram_ops_test.py
hist = histogram_ops.histogram_fixed_width(
    values=constant_op.constant(
        [-(2**31), 2**31 - 1], dtype=dtypes.int32
    ),
    value_range=constant_op.constant(
        [-(2**31), 2**31 - 1], dtype=dtypes.int32
    ),
    nbins=2,
)
self.assertAllEqual(hist, [1, 1])
