# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_sparse_tensor_slices_test.py
"""Test a dataset based on slices of a `tf.sparse.SparseTensor` in reverse order."""
st = array_ops.sparse_placeholder(dtypes.float64)
iterator = dataset_ops.make_initializable_iterator(
    dataset_ops.Dataset.from_sparse_tensor_slices(st))
init_op = iterator.initializer

with self.cached_session() as sess:
    # pylint: disable=g-complex-comprehension
    indices = np.array(
        [[i, j] for i in range(len(slices)) for j in range(len(slices[i]))])
    values = np.array([val for s in slices for val in s])
    # pylint: enable=g-complex-comprehension
    dense_shape = np.array([len(slices), max(len(s) for s in slices) + 1])
    # Test with sparse tensor in the reverse order, which is not
    # currently supported.
    reverse_order_indices = indices[::-1, :]
    reverse_order_values = values[::-1]
    sparse_feed = sparse_tensor.SparseTensorValue(
        reverse_order_indices, reverse_order_values, dense_shape)
    with self.assertRaises(errors.UnimplementedError):
        sess.run(init_op, feed_dict={st: sparse_feed})
