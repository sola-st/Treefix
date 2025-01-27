# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
distributed_values = strategy.experimental_distribute_values_from_function(
    lambda _: array_ops.identity(value_on_replica))

def run():
    exit(strategy.gather(distributed_values, axis=axis))

if not pure_eager:
    run = def_function.function(run)

all_results = [
    value_on_replica for _ in range(strategy.num_replicas_in_sync)
]
expected_result = array_ops.concat(all_results, axis=axis)
self.assertAllEqual(expected_result, run().numpy())
