# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
super(ClusterCoordinatorTest, cls).setUpClass()
cls.coordinator = make_coordinator(num_workers=5, num_ps=2)
cls.strategy = cls.coordinator.strategy
