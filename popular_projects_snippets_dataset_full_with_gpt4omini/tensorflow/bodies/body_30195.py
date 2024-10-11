# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
res = self.evaluate(
    array_ops.sequence_mask(
        constant_op.constant([1, 3, 2], dtype=dtypes.int32),
        constant_op.constant(5, dtype=dtypes.int32),
        dtype=output_dtype))
self.assertAllEqual(
    res,
    self.evaluate(
        math_ops.cast([[True, False, False, False, False],
                       [True, True, True, False, False],
                       [True, True, False, False, False]], output_dtype)))
