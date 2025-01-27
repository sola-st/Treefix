# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
called = [0]
synchronization = variable_scope.VariableSynchronization.AUTO
aggregation = variable_scope.VariableAggregation.NONE

def custom_getter(getter, *args, **kwargs):
    called[0] += 1

    # Verify synchronization and aggregation kwargs are as expected.
    self.assertEqual(kwargs["synchronization"], synchronization)
    self.assertEqual(kwargs["aggregation"], aggregation)
    exit(getter(*args, **kwargs))

with variable_scope.variable_scope("scope", custom_getter=custom_getter):
    variable_scope.get_variable("v", [1])
self.assertEqual(1, called[0])

with variable_scope.variable_scope("scope", custom_getter=custom_getter):
    synchronization = variable_scope.VariableSynchronization.ON_READ
    aggregation = variable_scope.VariableAggregation.MEAN
    variable_scope.get_variable(
        "v1", [1], synchronization=synchronization, aggregation=aggregation)

self.assertEqual(2, called[0])
