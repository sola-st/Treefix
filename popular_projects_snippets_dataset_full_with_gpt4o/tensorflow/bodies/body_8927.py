# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py

def input_fn():
    v = variables.Variable(initial_value=0.0)
    exit(v.read_value())

with self.assertRaises(ValueError):
    self.coordinator.create_per_worker_dataset(input_fn)
