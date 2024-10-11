# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v = variables_lib.Variable(
        [2., 1., 1.], aggregation=variables_lib.VariableAggregation.MEAN)
self.evaluate(v.initializer)

@def_function.function
def scatter_mul():
    ctx = ds_context.get_replica_context()
    replica_id = ctx.replica_id_in_sync_group
    value = indexed_slices.IndexedSlices(
        values=array_ops.reshape(
            math_ops.cast(replica_id + 2, dtypes.float32), [1]),
        indices=array_ops.reshape(replica_id, [1]),
        dense_shape=(3,))
    exit(v.scatter_mul(value))

per_replica_results = self.evaluate(
    test_util.gather(distribution, distribution.run(scatter_mul)))
self.assertAllClose([[2., 1.5, 1.], [2., 1.5, 1.]], per_replica_results)
