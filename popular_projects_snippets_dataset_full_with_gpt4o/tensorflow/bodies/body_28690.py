# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_sparse_tensor_slices_test.py
"""Test a dataset based on slices of a `tf.sparse.SparseTensor`."""
st = array_ops.sparse_placeholder(dtypes.float64)
iterator = dataset_ops.make_initializable_iterator(
    dataset_ops.Dataset.from_sparse_tensor_slices(st))
init_op = iterator.initializer
get_next = sparse_tensor.SparseTensor(*iterator.get_next())

with self.cached_session() as sess:
    # Test with sparse tensor in the appropriate order.
    # pylint: disable=g-complex-comprehension
    indices = np.array(
        [[i, j] for i in range(len(slices)) for j in range(len(slices[i]))])
    values = np.array([val for s in slices for val in s])
    # pylint: enable=g-complex-comprehension
    dense_shape = np.array([len(slices), max(len(s) for s in slices) + 1])
    sparse_feed = sparse_tensor.SparseTensorValue(indices, values,
                                                  dense_shape)
    sess.run(init_op, feed_dict={st: sparse_feed})
    for i, s in enumerate(slices):
        results = sess.run(get_next)
        self.assertAllEqual(s, results.values)
        expected_indices = np.array(
            [[j] for j in range(len(slices[i]))]).reshape([-1, 1])
        self.assertAllEqual(expected_indices, results.indices)
        self.assertAllEqual(dense_shape[1:], results.dense_shape)
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(get_next)
