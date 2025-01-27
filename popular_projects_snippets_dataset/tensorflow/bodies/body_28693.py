# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_sparse_tensor_slices_test.py
"""Test a dataset based on invalid `tf.sparse.SparseTensor`."""
st = array_ops.sparse_placeholder(dtypes.float64)
iterator = dataset_ops.make_initializable_iterator(
    dataset_ops.Dataset.from_sparse_tensor_slices(st))
init_op = iterator.initializer

with self.cached_session() as sess:
    # Test with an empty sparse tensor but with non empty values.
    empty_indices = np.empty((0, 4), dtype=np.int64)
    non_empty_values = [1, 2, 3, 4]
    empty_dense_shape = [0, 4, 37, 9]
    sparse_feed = sparse_tensor.SparseTensorValue(empty_indices,
                                                  non_empty_values,
                                                  empty_dense_shape)
    # Here, we expect the test to fail when running the feed.
    with self.assertRaises(errors.InvalidArgumentError):
        sess.run(init_op, feed_dict={st: sparse_feed})
