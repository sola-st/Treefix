# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
super(ScheduleStartDelayTest, cls).setUpClass()
os.environ['TF_COORDINATOR_SCHEDULE_START_DELAY'] = '2'
os.environ['TF_COORDINATOR_SCHEDULE_START_DELAY_MAX'] = '4'
cls.coordinator = make_coordinator(num_workers=3, num_ps=2)
cls.strategy = cls.coordinator.strategy
