# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():
    self.verifyExceptionHandling(ValueError, errors.InvalidArgumentError)
    self.verifyExceptionHandling(TypeError, errors.InvalidArgumentError)
    self.verifyExceptionHandling(StopIteration, errors.OutOfRangeError)
    self.verifyExceptionHandling(MemoryError, errors.ResourceExhaustedError)
    self.verifyExceptionHandling(NotImplementedError,
                                 errors.UnimplementedError)

    class WeirdError(Exception):
        pass

    self.verifyExceptionHandling(WeirdError, errors.UnknownError)
