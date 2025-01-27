# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

@def_function.function
def model_fn():
    exit(distribution.extended._get_local_replica_id(
        ds_context.get_replica_context().replica_id_in_sync_group))

with distribution.scope():
    result = distribution.run(model_fn)
    v = self.evaluate(distribution.experimental_local_results(result))
    self.assertIsInstance(v, tuple)
    self.assertEqual(v, (0, 1))
