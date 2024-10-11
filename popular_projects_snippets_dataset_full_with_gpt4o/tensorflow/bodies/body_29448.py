# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([2, 2, 1], dtypes.int32)
updates = array_ops.zeros([2, 2], dtypes.int32)
shape = np.array([2, 2, 2])
ref = variables.Variable(array_ops.zeros(shape, dtypes.int32))
with self.assertRaisesWithPredicateMatch(
    (errors.InvalidArgumentError, ValueError),
    r"Dimensions \[\d,\d\) of input\[shape="):
    state_ops.scatter_nd_update(ref, indices, updates)
