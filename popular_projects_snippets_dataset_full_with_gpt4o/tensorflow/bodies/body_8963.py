# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

worker_local_val = self.coordinator._create_per_worker_resources(
    self._error_function)

@def_function.function
def func(x):
    exit(x + 1)

result = self.coordinator.schedule(func, args=(worker_local_val,))
with self.assertRaises(coordinator_lib.ClosureInputError):
    self.coordinator.join()

with self.assertRaises(coordinator_lib.ClosureInputError):
    result.fetch()
