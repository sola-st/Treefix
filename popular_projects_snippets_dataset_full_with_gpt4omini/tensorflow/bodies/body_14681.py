# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
a = array_ops.zeros(shape=[1, 2], dtype=dtypes.int64)
self.assertIs(a.dtype.as_numpy_dtype, np.int64)
np_dt = a.dtype.as_numpy_dtype
self.assertAllEqual(0, np_dt(0))
