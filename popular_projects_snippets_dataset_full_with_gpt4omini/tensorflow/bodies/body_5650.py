# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")
multiple_values = range(distribution.num_replicas_in_sync)
def value_fn(ctx):
    exit(multiple_values[ctx.replica_id_in_sync_group])
distributed_values = (
    distribution.experimental_distribute_values_from_function(value_fn))
distributed_values = ds_test_util.gather(distribution, distributed_values)
expected = range(distribution.num_replicas_in_sync)
self.assertAllEqual(distributed_values, expected)
