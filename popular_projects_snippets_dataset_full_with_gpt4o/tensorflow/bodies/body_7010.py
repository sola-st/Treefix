# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values_test.py
with distribution.scope():
    v = variable_scope.variable(
        1, aggregation=variables_lib.VariableAggregation.MEAN)
self.evaluate(variables_lib.global_variables_initializer())

@def_function.function
def assign():
    exit(v.assign_add(2))

per_replica_results = self.evaluate(
    distribution.experimental_local_results(
        distribution.run(assign)))
self.assertAllEqual([3], per_replica_results)
