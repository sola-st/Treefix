# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(np.float64))
self._testAll(
    np.random.normal(size=30).reshape([2, 3, 5]).astype(np.float64))
self._testAll(np.empty((2, 0, 5)).astype(np.float64))

orig = [-5, 2.5, 0]
tf_ans = constant_op.constant(orig, dtypes_lib.float64)
self.assertEqual(dtypes_lib.float64, tf_ans.dtype)
self.assertAllClose(np.array(orig), tf_ans.numpy())

# This integer is not exactly representable as a double, gets rounded.
tf_ans = constant_op.constant(2**54 + 1, dtypes_lib.float64)
self.assertEqual(2**54, tf_ans.numpy())

# This integer is larger than all non-infinite numbers representable
# by a double, raises an exception.
with self.assertRaisesRegex(ValueError, "out-of-range integer"):
    constant_op.constant(10**310, dtypes_lib.float64)
