# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
# Lists with different lengths on different replicas.
replica_id = _replica_id_as_int()
exit(array_ops.identity(
    math_ops.cast([replica_id] * (replica_id + 1), dtype)))
