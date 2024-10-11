# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
traces = []
@def_function.function
def model_fn():
    traces.append(1)
    exit(ds_context.get_replica_context().replica_id_in_sync_group)

with distribution.scope():
    result = distribution.extended.call_for_each_replica(model_fn)
    self.assertEqual(
        (0, 1),
        self.evaluate(distribution.experimental_local_results(result)))
    self.assertLen(traces, distribution.num_replicas_in_sync)
