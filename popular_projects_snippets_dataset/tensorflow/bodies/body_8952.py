# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
del os.environ['TF_COORDINATOR_SCHEDULE_START_DELAY']
del os.environ['TF_COORDINATOR_SCHEDULE_START_DELAY_MAX']
super(ScheduleStartDelayTest, cls).tearDownClass()
