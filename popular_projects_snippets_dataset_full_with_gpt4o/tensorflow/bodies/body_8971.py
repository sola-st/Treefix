# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
super(StrategyIntegrationTest, cls).setUpClass()
cls.coordinator = make_coordinator(num_workers=1, num_ps=1)
cls.strategy = cls.coordinator.strategy
