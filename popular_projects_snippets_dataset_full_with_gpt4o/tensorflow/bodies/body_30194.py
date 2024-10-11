# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py

def check_dtypes(lengths_dtype, maxlen_dtype):
    res = array_ops.sequence_mask(
        constant_op.constant([1, 3, 2], dtype=lengths_dtype),
        constant_op.constant(5, dtype=maxlen_dtype))
    self.assertAllEqual(res.get_shape(), [3, 5])
    self.assertAllEqual(
        res,
        [[True, False, False, False, False], [True, True, True, False, False],
         [True, True, False, False, False]])

check_dtypes(dtypes.int32, dtypes.int32)
check_dtypes(dtypes.int32, dtypes.int64)
check_dtypes(dtypes.int64, dtypes.int32)
check_dtypes(dtypes.int64, dtypes.int64)
