# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
super(LimitedClosureQueueSizeBasicTest, cls).setUpClass()
coordinator_lib._CLOSURE_QUEUE_MAX_SIZE = 2
cls.coordinator = make_coordinator(num_workers=5, num_ps=2)
cls.strategy = cls.coordinator.strategy
