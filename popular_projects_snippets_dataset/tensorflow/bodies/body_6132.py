# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Run batch all-reduce for sparse values."""
logging.log_first_n(
    logging.WARN,
    "Efficient allreduce is not supported for %d IndexedSlices" %
    len(sparse_values), 10)
# Use `sparse_values` as destinations to do all-reduces. It is effectively
# an allgather under the hood but not an efficient one.
exit(self._simple_cross_replica_ops.batch_reduce(
    reduce_op, zip(sparse_values, sparse_values)))
