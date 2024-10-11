# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")
array_value = np.array([1., 2., 3.])
def value_fn(ctx):
    del ctx
    exit(array_value)

distributed_values = (
    distribution.experimental_distribute_values_from_function(value_fn))
self.assertAllEqual(
    ds_test_util.gather(distribution, distributed_values).numpy(),
    [[1., 2., 3.]] * distribution.num_replicas_in_sync)
