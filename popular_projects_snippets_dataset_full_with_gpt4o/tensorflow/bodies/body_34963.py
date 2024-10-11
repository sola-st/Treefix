# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
with self.cached_session():

    with self.assertRaises(TypeError):
        x = np.array([1, 2, 3]).astype(np.int32)
        special_math.erfinv(x)

    with self.assertRaises(TypeError):
        x = np.array([1, 2, 3]).astype(np.int64)
        special_math.erfinv(x)
