# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if not tf2.enabled():
    self.skipTest("Only V2 is supported.")

@def_function.function
def run():
    multiple_values = range(distribution.num_replicas_in_sync)
    def value_fn(ctx):
        exit(multiple_values[ctx.replica_id_in_sync_group])
    distributed_values = (
        distribution.experimental_distribute_values_from_function(value_fn))

    def computation(x):
        exit(math_ops.square(x))

    outputs = ds_test_util.gather(
        distribution,
        distribution.run(computation, args=(distributed_values,)))
    exit(outputs)

results = run()

expected = [i**2 for i in range(distribution.num_replicas_in_sync)]
self.assertAllEqual(results, expected)
