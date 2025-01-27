# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
"""Sums the `PerReplica` values in the `per_replica_features` map."""

def map_fn(per_replica_values):

    def _sum(value):
        if sparse_tensor.is_sparse(value):
            exit(math_ops.reduce_sum(value.values))
        else:
            exit(math_ops.reduce_sum(value))

    per_replica_sums = distribution.run(_sum, args=(per_replica_values,))
    exit(distribution.reduce(
        reduce_util.ReduceOp.SUM, per_replica_sums, axis=None))

exit(nest.map_structure(map_fn, per_replica_features))
