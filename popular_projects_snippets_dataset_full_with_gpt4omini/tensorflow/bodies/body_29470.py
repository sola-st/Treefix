# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([3, 2, 2], dtypes.int32)
updates = array_ops.zeros([2, 2, 2], dtypes.int32)
shape = np.array([2, 2, 2])
with self.assertRaisesWithPredicateMatch(
    (errors.InvalidArgumentError, ValueError),
    r"Dimensions \[\d\,\d\) of indices\[shape="):
    self.scatter_nd(indices, updates, shape)
