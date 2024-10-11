# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
for rank in range(1, 4):
    # Create a dummy input. When rank=3, shape=[2, 4, 6].
    shape = np.arange(1, rank + 1) * 2
    before = np.arange(np.prod(shape)).reshape(shape)

    # Make entries sparse.
    before *= np.random.binomial(1, .2, before.shape)
    dense_shape = before.shape
    indices = np.array(np.where(before)).T
    values = before[before != 0]

    # Try every possible valid value of axis.
    for axis in range(-rank - 1, rank):
        expected_after = np.expand_dims(before, axis)

        for axis_as_tensor in [False, True]:
            dense_shape_t = constant_op.constant(dense_shape, dtype=dtypes.int64)
            indices_t = constant_op.constant(indices)
            values_t = constant_op.constant(values)
            before_t = sparse_tensor.SparseTensor(
                indices=indices_t, values=values_t, dense_shape=dense_shape_t)

            if axis_as_tensor:
                axis = constant_op.constant(axis)

            s = sparse_ops.sparse_expand_dims(before_t, axis)
            d = sparse_ops.sparse_to_dense(s.indices, s.dense_shape, s.values)
            self.assertAllEqual(self.evaluate(d), expected_after)
