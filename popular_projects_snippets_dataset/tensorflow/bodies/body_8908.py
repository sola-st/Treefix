# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
super(TestCaseWithErrorReportingThread, self).tearDown()
if ErrorReportingThread.error:
    raise ErrorReportingThread.error  # pylint: disable=raising-bad-type
