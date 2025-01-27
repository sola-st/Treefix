# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
in_types = (dtypes.float32, dtypes.float64)
out_types = (dtypes.complex64, dtypes.complex128)
for in_type in in_types:
    for out_type in out_types:
        lo, hi = in_type.min, in_type.max
        x = constant_op.constant([lo, lo + 1, lo // 2, hi // 2, hi - 1, hi],
                                 dtype=in_type)
        y = math_ops.saturate_cast(x, dtype=out_type)
        self.assertEqual(y.dtype, out_type)
        x, y = self.evaluate([x, y])
        correct = np.maximum(out_type.real_dtype.min,
                             np.minimum(out_type.real_dtype.max, x))
        self.assertAllEqual(correct, y)
