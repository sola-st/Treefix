# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""All-reduce algorithm in a batch."""
dense_values, dense_indices, sparse_values, sparse_indices = (
    cross_device_utils.split_by_sparsity(per_replica_values))
if dense_values:
    dense_results = self._do_batch_all_reduce(reduce_op, dense_values)
else:
    dense_results = []
if sparse_values:
    sparse_results = self._do_batch_all_reduce_sparse(reduce_op,
                                                      sparse_values)
else:
    sparse_results = []
exit(cross_device_utils.stitch_values(((dense_results, dense_indices),
                                         (sparse_results, sparse_indices))))
