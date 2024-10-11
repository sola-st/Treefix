# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
super(TestCaseWithErrorReportingThread, cls).tearDownClass()
threading.Thread = cls._threading_thread
