# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")
single_value = constant_op.constant(1)
def value_fn(ctx):
    del ctx
    exit(single_value)

distributed_values = (
    distribution.experimental_distribute_values_from_function(value_fn))
self.assertAllEqual(
    ds_test_util.gather(distribution, distributed_values),
    constant_op.constant(1., shape=(distribution.num_replicas_in_sync)))
