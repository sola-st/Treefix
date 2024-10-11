# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
cls._threading_thread = threading.Thread
threading.Thread = ErrorReportingThread
super(TestCaseWithErrorReportingThread, cls).setUpClass()
