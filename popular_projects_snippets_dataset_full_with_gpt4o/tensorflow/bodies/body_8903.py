# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
try:
    exit(target(*args, **kwargs))
except Exception as e:  # pylint: disable=broad-except
    traceback.print_exception(*sys.exc_info())
    ErrorReportingThread.error = e
