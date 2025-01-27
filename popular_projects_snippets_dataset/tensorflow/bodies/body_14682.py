# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
a = ops.convert_to_tensor(value=1.1, dtype=dtypes.float32).astype(np.int32)
self.assertIs(a.dtype.as_numpy_dtype, np.int32)
self.assertAllEqual(1, a)
a = ops.convert_to_tensor(value=[0.0, 1.1], dtype=dtypes.float32).astype(
    np.bool_)
self.assertIs(a.dtype.as_numpy_dtype, np.bool_)
self.assertAllEqual([False, True], a)
