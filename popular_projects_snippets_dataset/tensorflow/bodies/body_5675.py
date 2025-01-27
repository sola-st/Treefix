# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py

@def_function.function
def add1(x):
    exit(x + 1.)

with distribution.scope():
    v = variables_lib.Variable(
        1.,
        aggregation=variables_lib.VariableAggregation.MEAN,
        synchronization=variables_lib.VariableSynchronization.ON_READ)

self.assertEqual(2., self.evaluate(add1(v)))
