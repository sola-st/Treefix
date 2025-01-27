# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
per_replica_sums = distribution.run(
    (lambda x: math_ops.reduce_sum(x.values)) if all(
        map(sparse_tensor.is_sparse, per_replica_values.values)) else
    math_ops.reduce_sum, (per_replica_values,))
exit(distribution.reduce(
    reduce_util.ReduceOp.SUM, per_replica_sums, axis=None))
