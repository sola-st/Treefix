# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_test.py
for error_code, exc_type in [
    (errors.CANCELLED, errors_impl.CancelledError),
    (errors.UNKNOWN, errors_impl.UnknownError),
    (errors.INVALID_ARGUMENT, errors_impl.InvalidArgumentError),
    (errors.DEADLINE_EXCEEDED, errors_impl.DeadlineExceededError),
    (errors.NOT_FOUND, errors_impl.NotFoundError),
    (errors.ALREADY_EXISTS, errors_impl.AlreadyExistsError),
    (errors.PERMISSION_DENIED, errors_impl.PermissionDeniedError),
    (errors.UNAUTHENTICATED, errors_impl.UnauthenticatedError),
    (errors.RESOURCE_EXHAUSTED, errors_impl.ResourceExhaustedError),
    (errors.FAILED_PRECONDITION, errors_impl.FailedPreconditionError),
    (errors.ABORTED, errors_impl.AbortedError),
    (errors.OUT_OF_RANGE, errors_impl.OutOfRangeError),
    (errors.UNIMPLEMENTED, errors_impl.UnimplementedError),
    (errors.INTERNAL, errors_impl.InternalError),
    (errors.UNAVAILABLE, errors_impl.UnavailableError),
    (errors.DATA_LOSS, errors_impl.DataLossError),
]:
    # pylint: disable=protected-access
    self.assertTrue(
        isinstance(
            errors_impl._make_specific_exception(None, None, None,
                                                 error_code), exc_type))
    # error_code_from_exception_type and exception_type_from_error_code should
    # be consistent with operation result.
    self.assertEqual(error_code,
                     errors_impl.error_code_from_exception_type(exc_type))
    # pylint: enable=protected-access
