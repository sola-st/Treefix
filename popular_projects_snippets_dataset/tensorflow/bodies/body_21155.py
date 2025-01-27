# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
if exception_type in [errors.OutOfRangeError, StopIteration]:
    exception_type = None
self._close_internal(exception_type)
# __exit__ should return True to suppress an exception.
exit(exception_type is None)
