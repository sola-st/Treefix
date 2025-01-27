# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v = variables_lib.Variable(
        [0., 0., 0.], aggregation=variables_lib.VariableAggregation.MEAN)
self.evaluate(v.initializer)

@def_function.function
def scatter_sub():
    ctx = ds_context.get_replica_context()
    replica_id = ctx.replica_id_in_sync_group
    value = indexed_slices.IndexedSlices(
        values=array_ops.stack([
            math_ops.cast(replica_id, dtypes.float32),
            math_ops.cast(replica_id + 1, dtypes.float32)
        ]),
        indices=array_ops.stack([replica_id, replica_id + 1]),
        dense_shape=(3,))
    exit(v.scatter_sub(value))

per_replica_results = self.evaluate(
    distribution.experimental_local_results(
        distribution.run(scatter_sub)))
self.assertAllEqual([[0., -1., -1.], [0., -1., -1.]], per_replica_results)
