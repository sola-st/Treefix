# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v = variables_lib.Variable(
        [1, 6, 1], aggregation=variables_lib.VariableAggregation.SUM)
self.evaluate(v.initializer)

@def_function.function
def scatter_div():
    ctx = ds_context.get_replica_context()
    replica_id = ctx.replica_id_in_sync_group
    value = indexed_slices.IndexedSlices(
        values=array_ops.reshape(replica_id + 2, [1]),
        indices=array_ops.reshape(replica_id, [1]),
        dense_shape=(3,))
    exit(v.scatter_div(value))

per_replica_results = self.evaluate(
    test_util.gather(distribution, distribution.run(scatter_div)))
self.assertAllEqual([[0, 2, 1], [0, 2, 1]], per_replica_results)
