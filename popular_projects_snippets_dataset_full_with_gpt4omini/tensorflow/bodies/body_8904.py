# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
assert 'target' in kwargs
target = kwargs['target']

@functools.wraps(target)
def wrapped_target(*args, **kwargs):
    try:
        exit(target(*args, **kwargs))
    except Exception as e:  # pylint: disable=broad-except
        traceback.print_exception(*sys.exc_info())
        ErrorReportingThread.error = e

kwargs['target'] = wrapped_target
super(ErrorReportingThread, self).__init__(*args, **kwargs)
