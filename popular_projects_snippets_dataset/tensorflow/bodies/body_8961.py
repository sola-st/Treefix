# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self.skipTest('TODO(b/211502459): Fix this in OSS test.')

result = self.coordinator.schedule(self._error_function)

with self.assertRaises(errors.InvalidArgumentError):
    result.fetch()

# Clear the error.
with self.assertRaises(errors.InvalidArgumentError):
    self.coordinator.join()
