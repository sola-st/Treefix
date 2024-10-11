# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
self.assertIs(dtypes.float32,
              check_ops.assert_same_float_dtype(None, None))
self.assertIs(dtypes.float32, check_ops.assert_same_float_dtype([], None))
self.assertIs(dtypes.float32,
              check_ops.assert_same_float_dtype([], dtypes.float32))
self.assertIs(dtypes.float32,
              check_ops.assert_same_float_dtype(None, dtypes.float32))
self.assertIs(dtypes.float32,
              check_ops.assert_same_float_dtype([None, None], None))
self.assertIs(
    dtypes.float32,
    check_ops.assert_same_float_dtype([None, None], dtypes.float32))

const_float = constant_op.constant(3.0, dtype=dtypes.float32)
self.assertIs(
    dtypes.float32,
    check_ops.assert_same_float_dtype([const_float], dtypes.float32))
self.assertRaises(ValueError, check_ops.assert_same_float_dtype,
                  [const_float], dtypes.int32)

sparse_float = sparse_tensor.SparseTensor(
    constant_op.constant([[111], [232]], dtypes.int64),
    constant_op.constant([23.4, -43.2], dtypes.float32),
    constant_op.constant([500], dtypes.int64))
self.assertIs(dtypes.float32,
              check_ops.assert_same_float_dtype([sparse_float],
                                                dtypes.float32))
self.assertRaises(ValueError, check_ops.assert_same_float_dtype,
                  [sparse_float], dtypes.int32)
self.assertRaises(ValueError, check_ops.assert_same_float_dtype,
                  [const_float, None, sparse_float], dtypes.float64)

self.assertIs(dtypes.float32,
              check_ops.assert_same_float_dtype(
                  [const_float, sparse_float]))
self.assertIs(dtypes.float32,
              check_ops.assert_same_float_dtype(
                  [const_float, sparse_float], dtypes.float32))

const_int = constant_op.constant(3, dtype=dtypes.int32)
self.assertRaises(ValueError, check_ops.assert_same_float_dtype,
                  [sparse_float, const_int])
self.assertRaises(ValueError, check_ops.assert_same_float_dtype,
                  [sparse_float, const_int], dtypes.int32)
self.assertRaises(ValueError, check_ops.assert_same_float_dtype,
                  [sparse_float, const_int], dtypes.float32)
self.assertRaises(ValueError, check_ops.assert_same_float_dtype,
                  [const_int])
