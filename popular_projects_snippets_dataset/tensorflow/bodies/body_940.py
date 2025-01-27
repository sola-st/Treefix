# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sparse_to_dense_op_test.py
feed_sparse_indices = array_ops.placeholder(dtypes.int32)
feed_dict = {feed_sparse_indices: sparse_indices}
exit(sparse_ops.sparse_to_dense(
    feed_sparse_indices,
    output_size,
    sparse_values,
    default_value=default_value,
    validate_indices=validate_indices).eval(feed_dict=feed_dict))
