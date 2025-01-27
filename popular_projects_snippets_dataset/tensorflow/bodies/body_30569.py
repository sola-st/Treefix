# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
zero_int32 = math_ops.cast(0, dtypes.int32)
zero_int64 = math_ops.cast(0, dtypes.int64)
zero_float32 = math_ops.cast(0, dtypes.float32)
zero_float64 = math_ops.cast(0, dtypes.float64)

self.assertEqual(math_ops.range(zero_int32, 0, 1).dtype, dtypes.int32)
self.assertEqual(math_ops.range(zero_int64, 0, 1).dtype, dtypes.int64)
self.assertEqual(math_ops.range(zero_float32, 0, 1).dtype, dtypes.float32)
self.assertEqual(math_ops.range(zero_float64, 0, 1).dtype, dtypes.float64)

self.assertEqual(
    math_ops.range(zero_int32, zero_int64, 1).dtype, dtypes.int64)
self.assertEqual(
    math_ops.range(zero_int64, zero_float32, 1).dtype, dtypes.float32)
self.assertEqual(
    math_ops.range(zero_float32, zero_float64, 1).dtype, dtypes.float64)
self.assertEqual(
    math_ops.range(zero_float64, zero_int32, 1).dtype, dtypes.float64)

self.assertEqual(
    math_ops.range(0, 0, 1, dtype=dtypes.int32).dtype, dtypes.int32)
self.assertEqual(
    math_ops.range(0, 0, 1, dtype=dtypes.int64).dtype, dtypes.int64)
self.assertEqual(
    math_ops.range(0, 0, 1, dtype=dtypes.float32).dtype, dtypes.float32)
self.assertEqual(
    math_ops.range(0, 0, 1, dtype=dtypes.float64).dtype, dtypes.float64)
