# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

@def_function.function
def func_0():
    exit(1.0)

@def_function.function
def func_1(x):
    exit(x + 1.0)

remote_v = self.coordinator.schedule(func_0)
with self.assertRaises(ValueError):
    self.coordinator.schedule(func_1, args=(remote_v,))
