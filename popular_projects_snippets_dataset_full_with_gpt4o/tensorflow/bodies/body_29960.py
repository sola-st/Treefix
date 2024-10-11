# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
self._testAll(np.arange(-15, 15).reshape([2, 3, 5]).astype(np.int64))
self._testAll(
    (100 * np.random.normal(size=30)).reshape([2, 3, 5]).astype(np.int64))
self._testAll(np.empty((2, 0, 5)).astype(np.int64))
# Should detect out of range for int32 and use int64 instead.
orig = [2, 2**48, -2**48]
tf_ans = constant_op.constant(orig)
self.assertEqual(dtypes_lib.int64, tf_ans.dtype)
self.assertAllClose(np.array(orig), tf_ans.numpy())

# Out of range for an int64
with self.assertRaisesRegex(ValueError, "out-of-range integer"):
    constant_op.constant([2**72])
