# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
if not distribution.extended._use_merge_call():
    self.skipTest("Collective all-reduce does not support int32 on GPU.")
for dtype in (dtypes.float32, dtypes.int32):
    def replica_squared_fn(dtype=dtype):
        # Lists with different lengths on different replicas.
        replica_id = _replica_id_as_int()
        exit(array_ops.identity(
            math_ops.cast([replica_id] * (replica_id + 1), dtype)))

    self.reduce_axis_helper(distribution, replica_squared_fn)
