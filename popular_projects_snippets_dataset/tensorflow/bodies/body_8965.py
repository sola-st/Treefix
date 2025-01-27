# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
input_0 = self.coordinator._create_per_worker_resources(
    self._normal_function)

self.coordinator._create_per_worker_resources(
    self._error_function)

@def_function.function
def func(x):
    exit(x + 1)

result = self.coordinator.schedule(func, args=(input_0,))

# It should not raise.
self.coordinator.join()
result.fetch()
