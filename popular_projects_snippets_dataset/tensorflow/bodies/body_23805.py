# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
a = np.array([31], float_type)
b = np.array([15], float_type)
self.assertFalse(a.__eq__(b))
