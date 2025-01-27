# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
x = next(iterator)
# Reduce to convert PerReplica values to single value
reduced_value = self.strategy.reduce('MEAN', x, axis=None)
v.assign_add(reduced_value)
