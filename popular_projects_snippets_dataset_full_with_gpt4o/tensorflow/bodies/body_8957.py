# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
for _ in range(3):
    self.coordinator.schedule(self._normal_function)
self.coordinator.schedule(self._error_function)
with self.assertRaises(errors.InvalidArgumentError):
    self.coordinator.join()
