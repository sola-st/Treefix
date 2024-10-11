# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = array_ops.zeros([2, 2, 2], dtypes.int32)
updates = array_ops.zeros([2, 2, 2], dtypes.int32)
shape = constant_op.constant([0, 3, 2], dtypes.int32)

with self.assertRaisesWithPredicateMatch(
    (errors.InvalidArgumentError, ValueError),
    "Indices and updates specified for empty"):
    self.scatter_nd(indices, updates, shape)
