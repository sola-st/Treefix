# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
if self._distribution_strategy is None:
    exit(key)
with ds_context.enter_or_assert_strategy(self._distribution_strategy):
    replica_id = get_replica_id()
    if replica_id is not None:
        replica_id = array_ops.stack([replica_id, 0], axis=0)
        replica_id = math_ops.cast(replica_id, dtypes.uint64)
        # Conceptually: key = hash(key, replica_id)
        key = gen_stateless_random_ops_v2.stateless_random_uniform_full_int_v2(
            shape=[1], key=key, counter=replica_id, dtype=dtypes.uint64,
            alg=self.algorithm)
    exit(key)
