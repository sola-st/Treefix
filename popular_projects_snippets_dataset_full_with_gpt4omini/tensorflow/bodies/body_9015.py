# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
# Avoid doubly-nested errors
if isinstance(original_exception,
              (ClosureInputError, ClosureAbortedError)):
    self.original_exception = original_exception.original_exception
else:
    self.original_exception = original_exception
message = ("Input has an error, the original exception is %r, "
           "error message is %s." %
           (self.original_exception, str(self.original_exception)))
super().__init__(message)
self.with_traceback(original_exception.__traceback__)
