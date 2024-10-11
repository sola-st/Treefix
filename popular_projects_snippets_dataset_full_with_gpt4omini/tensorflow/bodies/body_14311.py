# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_dtypes_test.py
np_dtypes.set_allow_float64(False)
np_dtypes.set_prefer_float32(prefer_f32)
self.assertEqual(dtypes.float32, np_dtypes.default_float_type())
self.assertEqual(dtypes.float32,
                 np_dtypes._result_type(np.zeros([], np.float64), 1.1))
