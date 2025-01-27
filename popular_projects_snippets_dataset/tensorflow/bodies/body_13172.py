# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = constant_op.constant([[0, 6, 2, 8, 4], [5, 1, 7, 3, 9]], dtype=dtype_in)
y, segments = nn_ops.isotonic_regression(x)
self.assertEqual(y.dtype, expected_dtype_out)
self.assertEqual(segments.dtype, dtypes.int32)
