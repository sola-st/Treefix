# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
super(ErrorReportingTest, cls).setUpClass()
cls.coordinator = make_coordinator(num_workers=3, num_ps=2)
cls.strategy = cls.coordinator.strategy

with cls.strategy.scope():
    cls.iteration = variables.Variable(initial_value=0.0)
