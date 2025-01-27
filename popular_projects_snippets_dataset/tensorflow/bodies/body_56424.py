# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_test.py
for exception_type in [
    (errors.CancelledError),
    (errors.UnknownError),
    (errors.InvalidArgumentError),
    (errors.DeadlineExceededError),
    (errors.NotFoundError),
    (errors.AlreadyExistsError),
    (errors.PermissionDeniedError),
    (errors.UnauthenticatedError),
    (errors.ResourceExhaustedError),
    (errors.FailedPreconditionError),
    (errors.AbortedError),
    (errors.OutOfRangeError),
    (errors.UnimplementedError),
    (errors.InternalError),
    (errors.UnavailableError),
    (errors.DataLossError),
]:
    e = exception_type(None, None, None)
    self.assertEqual(type(e.experimental_payloads), dict)
    self.assertEqual(len(e.experimental_payloads), 0)
