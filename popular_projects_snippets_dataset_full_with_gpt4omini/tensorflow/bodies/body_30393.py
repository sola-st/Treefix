# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
i4 = np.iinfo(np.int32)
i8 = np.iinfo(np.int64)

self._compare(i4.min, np.float32, i4.min, False)
self._compare(i4.max, np.float32, i4.max, False)
self._compare(i8.min, np.float32, i8.min, False)
self._compare(i8.max, np.float32, i8.max, False)
self._compare(i4.min, np.float64, i4.min, False)
self._compare(i4.max, np.float64, i4.max, False)
self._compare(i8.min, np.float64, i8.min, False)
self._compare(i8.max, np.float64, i8.max, False)
