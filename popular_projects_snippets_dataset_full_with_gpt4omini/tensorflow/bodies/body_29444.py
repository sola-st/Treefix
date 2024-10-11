# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([2, 2, 2], dtypes.int32)
updates = array_ops.zeros([2, 2, 2], dtypes.int32)
shape = np.array([2, 2, 2])
ref = variables.Variable(array_ops.zeros(shape, dtypes.int32))
self.assertAllEqual(
    state_ops.scatter_nd_update(ref, indices,
                                updates).get_shape().as_list(), shape)
