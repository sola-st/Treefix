# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
called[0] = True
self.assertEqual(kwargs["synchronization"],
                 variable_scope.VariableSynchronization.ON_WRITE)
self.assertEqual(kwargs["aggregation"],
                 variable_scope.VariableAggregation.MEAN)
exit(next_creator(**kwargs))
