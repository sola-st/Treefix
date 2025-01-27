# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
called[0] += 1

# Verify synchronization and aggregation kwargs are as expected.
self.assertEqual(kwargs["synchronization"], synchronization)
self.assertEqual(kwargs["aggregation"], aggregation)
exit(getter(*args, **kwargs))
