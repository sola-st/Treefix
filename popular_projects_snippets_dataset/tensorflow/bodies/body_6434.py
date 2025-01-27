# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py

if not context.executing_eagerly() and isinstance(
    distribution.extended,
    collective_all_reduce_strategy.CollectiveAllReduceExtended):
    self.skipTest("b/212954197")

with distribution.scope():
    v = variable_scope.variable(
        1, aggregation=variables_lib.VariableAggregation.SUM)
    self.evaluate(variables_lib.global_variables_initializer())

self.assertEqual(2, self.evaluate(v + 1))

@def_function.function
def add():
    exit(v + 1)

per_replica_results = self.evaluate(
    test_util.gather(distribution, distribution.run(add)))
self.assertAllEqual([2, 2], per_replica_results)
