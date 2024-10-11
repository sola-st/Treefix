# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
densified = self.evaluate(sparse_ops.sparse_tensor_to_dense(sp_t))

np_op = np.sum
tf_op = sparse_ops.sparse_reduce_sum
if not do_sum:
    np_op = np.max
    tf_op = sparse_ops.sparse_reduce_max

np_ans = densified
if reduction_axes is None:
    np_ans = np_op(np_ans, keepdims=keep_dims)
else:
    if not isinstance(reduction_axes, list):  # Single scalar.
        reduction_axes = [reduction_axes]
    reduction_axes = np.array(reduction_axes).astype(np.int32)
    # Handles negative axes.
    reduction_axes = (reduction_axes + ndims) % ndims
    # Loop below depends on sorted.
    reduction_axes.sort()
    for ra in reduction_axes.ravel()[::-1]:
        np_ans = np_op(np_ans, axis=ra, keepdims=keep_dims)

tf_ans = tf_op(sp_t, reduction_axes, keep_dims)
self.assertAllEqual(np_ans.shape, tf_ans.get_shape().as_list())
