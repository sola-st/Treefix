# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
self.cluster_coord = coordinator
self.strategy = self.cluster_coord.strategy
with self.cluster_coord.strategy.scope():
    self.build()
