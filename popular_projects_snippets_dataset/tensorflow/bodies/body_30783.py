# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/inplace_ops_test.py
with test_util.use_gpu():
    x = array_ops.ones([7, 3], dtypes.bool)
    y = np.ones([7, 3], dtypes.bool.as_numpy_dtype)
    self.assertAllClose(x, y)
    x = inplace_ops.inplace_update(x, [3], array_ops.ones([1, 3],
                                                          dtypes.bool))
    y[3, :] = True
    self.assertAllClose(x, y)
    x = inplace_ops.inplace_update(x, [-1],
                                   array_ops.zeros([1, 3], dtypes.bool))
    y[-1, :] = False
    self.assertAllClose(x, y)
    x = inplace_ops.inplace_update(x, 5, array_ops.zeros([3], dtypes.bool))
    y[5, :] = False
    self.assertAllClose(x, y)
