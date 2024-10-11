# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
with distribution.scope():
    v1 = variables_lib.Variable(
        0.0,
        aggregation=variables_lib.VariableAggregation.SUM,
        synchronization=variables_lib.VariableSynchronization.ON_READ)
    v2 = variables_lib.Variable(
        0.0,
        aggregation=variables_lib.VariableAggregation.SUM,
        synchronization=variables_lib.VariableSynchronization.ON_READ)

@def_function.function
def replica_fn():
    v1.assign_add(1.0)
    v2.assign_add(2.0)

distribution.run(replica_fn)
sum_v = v1 + v2
self.assertEqual(sum_v, 6.0)
