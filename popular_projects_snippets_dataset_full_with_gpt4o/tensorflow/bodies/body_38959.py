# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
densified = self.evaluate(sparse_ops.sparse_tensor_to_dense(sp_t))

np_ans = densified
if reduction_axes is None:
    if do_sum:
        np_ans = np.sum(np_ans, keepdims=keep_dims)
    else:
        np_ans = np.max(np_ans, keepdims=keep_dims)
else:
    if not isinstance(reduction_axes, list):  # Single scalar.
        reduction_axes = [reduction_axes]
    reduction_axes = np.array(reduction_axes).astype(np.int32)
    # Handles negative axes.
    reduction_axes = (reduction_axes + ndims) % ndims
    # Loop below depends on sorted.
    reduction_axes.sort()
    for ra in reduction_axes.ravel()[::-1]:
        if do_sum:
            np_ans = np.sum(np_ans, axis=ra, keepdims=keep_dims)
        else:
            np_ans = np.max(np_ans, axis=ra, keepdims=keep_dims)

with self.cached_session():
    if do_sum:
        tf_dense_ans = sparse_ops.sparse_reduce_sum(sp_t, reduction_axes,
                                                    keep_dims)
    else:
        tf_dense_ans = sparse_ops.sparse_reduce_max(sp_t, reduction_axes,
                                                    keep_dims)
    out_dense = self.evaluate(tf_dense_ans)

    if do_sum:
        tf_sparse_ans = sparse_ops.sparse_reduce_sum_sparse(sp_t,
                                                            reduction_axes,
                                                            keep_dims)
    else:
        tf_sparse_ans = sparse_ops.sparse_reduce_max_sparse(sp_t,
                                                            reduction_axes,
                                                            keep_dims)
    # Convert to dense for comparison purposes.
    out_sparse = sparse_ops.sparse_tensor_to_dense(tf_sparse_ans)

self.assertAllClose(np_ans, out_dense)
self.assertAllClose(np_ans, out_sparse)
