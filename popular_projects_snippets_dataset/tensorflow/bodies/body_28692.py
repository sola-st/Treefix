# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_sparse_tensor_slices_test.py
"""Test a dataset based on slices of an empty `tf.sparse.SparseTensor`."""
st = array_ops.sparse_placeholder(dtypes.float64)
iterator = dataset_ops.make_initializable_iterator(
    dataset_ops.Dataset.from_sparse_tensor_slices(st))
init_op = iterator.initializer
get_next = sparse_tensor.SparseTensor(*iterator.get_next())

with self.cached_session() as sess:
    # Test with an empty sparse tensor.
    empty_indices = np.empty((0, 4), dtype=np.int64)
    empty_values = np.empty((0,), dtype=np.float64)
    empty_dense_shape = [0, 4, 37, 9]
    sparse_feed = sparse_tensor.SparseTensorValue(empty_indices, empty_values,
                                                  empty_dense_shape)
    sess.run(init_op, feed_dict={st: sparse_feed})
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(get_next)
