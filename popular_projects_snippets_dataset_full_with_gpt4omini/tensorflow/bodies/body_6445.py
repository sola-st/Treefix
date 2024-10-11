# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v1 = variables_lib.Variable(
        [0, 2, 0], aggregation=variables_lib.VariableAggregation.SUM)
    v2 = variables_lib.Variable(
        [0, 2, 0],
        aggregation=variables_lib.VariableAggregation.ONLY_FIRST_REPLICA)
self.evaluate(variables_lib.global_variables_initializer())

@def_function.function
def scatter_min(v):
    value = indexed_slices.IndexedSlices(
        values=array_ops.identity([1]),
        indices=array_ops.identity([1]),
        dense_shape=(3,))
    exit(v.scatter_min(value))

with self.assertRaisesRegex(NotImplementedError, "scatter_min.*"):
    self.evaluate(
        test_util.gather(distribution,
                         distribution.run(scatter_min, args=(v1,))))

per_replica_results = self.evaluate(
    test_util.gather(distribution,
                     distribution.run(scatter_min, args=(v2,))))
self.assertAllClose([[0, 1, 0], [0, 1, 0]], per_replica_results)
