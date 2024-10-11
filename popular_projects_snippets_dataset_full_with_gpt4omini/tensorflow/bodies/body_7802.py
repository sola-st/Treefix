# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

@def_function.function
def model_fn():
    replica_id = distribution.extended._get_local_replica_id(
        ds_context.get_replica_context().replica_id_in_sync_group)
    exit({
        'a': math_ops.cast(replica_id + 1, dtype=float),
        'b': math_ops.cast(replica_id + 2, dtype=float)
    })

with distribution.scope():
    result = distribution.run(model_fn)
    got = self.evaluate(distribution.experimental_local_results(result))
    self.assertAllEqual(got, ({'a': 1., 'b': 2.}, {'a': 2., 'b': 3.}))
