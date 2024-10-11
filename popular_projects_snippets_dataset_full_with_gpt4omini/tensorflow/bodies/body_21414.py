# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""Create a new Coordinator.

    Args:
      clean_stop_exception_types: Optional tuple of Exception types that should
        cause a clean stop of the coordinator. If an exception of one of these
        types is reported to `request_stop(ex)` the coordinator will behave as
        if `request_stop(None)` was called.  Defaults to
        `(tf.errors.OutOfRangeError,)` which is used by input queues to signal
        the end of input. When feeding training data from a Python iterator it
        is common to add `StopIteration` to this list.
    """
if clean_stop_exception_types is None:
    clean_stop_exception_types = (errors.OutOfRangeError,)
self._clean_stop_exception_types = tuple(clean_stop_exception_types)
# Protects all attributes.
self._lock = threading.Lock()
# Event set when threads must stop.
self._stop_event = threading.Event()
# Python exc_info to report.
# If not None, it should hold the returned value of sys.exc_info(), which is
# a tuple containing exception (type, value, traceback).
self._exc_info_to_raise = None
# True if we have called join() already.
self._joined = False
# Set of threads registered for joining when join() is called.  These
# threads will be joined in addition to the threads passed to the join()
# call.  It's ok if threads are both registered and passed to the join()
# call.
self._registered_threads = set()
