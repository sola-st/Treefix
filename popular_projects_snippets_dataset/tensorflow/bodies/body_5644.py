# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")
tuple_value = (1., 2., 3.)
def value_fn(ctx):
    del ctx
    exit(tuple_value)
distributed_values = (
    distribution.experimental_distribute_values_from_function(value_fn))
distributed_values = ds_test_util.gather(distribution, distributed_values)

# Expected output for 2 replicas:
# ([1.0, 1.0], [2.0, 2.0], [3.0, 3.0])
expected = tuple([v for i in range(distribution.num_replicas_in_sync)]
                 for v in tuple_value)
self.assertAllEqual(distributed_values, expected)
