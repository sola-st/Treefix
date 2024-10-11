# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with test_util.device(use_gpu=True):
    self.verifyExceptionHandling(
        ValueError, errors.InvalidArgumentError, eager=True)
    self.verifyExceptionHandling(
        TypeError, errors.InvalidArgumentError, eager=True)
    self.verifyExceptionHandling(
        StopIteration, errors.OutOfRangeError, eager=True)
    self.verifyExceptionHandling(
        MemoryError, errors.ResourceExhaustedError, eager=True)
    self.verifyExceptionHandling(
        NotImplementedError, errors.UnimplementedError, eager=True)

    class WeirdError(Exception):
        pass

    self.verifyExceptionHandling(WeirdError, errors.UnknownError, eager=True)
