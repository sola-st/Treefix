# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
self._testUnaryOp(np_math_ops.argsort, np.argsort, 'argsort')

# Test stability
r = np.arange(100)
a = np.zeros(100)
np.testing.assert_equal(np_math_ops.argsort(a, kind='stable'), r)
