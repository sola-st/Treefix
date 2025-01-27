# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_dtypes_test.py
np_dtypes.set_allow_float64(True)
np_dtypes.set_prefer_float32(False)
self.assertEqual(dtypes.float64, np_dtypes.default_float_type())
self.assertEqual(dtypes.float64, np_dtypes._result_type(1.1))
self.assertEqual(dtypes.complex128, np_dtypes._result_type(1.j))
