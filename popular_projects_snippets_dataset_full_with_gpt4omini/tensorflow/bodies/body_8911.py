# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
cluster = self.coordinator._cluster
same_coordinator = coordinator_lib.ClusterCoordinator(self.strategy)
self.assertIs(self.coordinator, same_coordinator)
self.assertIs(cluster, same_coordinator._cluster)
