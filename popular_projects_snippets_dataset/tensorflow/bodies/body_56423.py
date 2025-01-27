# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_test.py
for code, expected_exception in [
    (1, errors.CancelledError),
    (2, errors.UnknownError),
    (3, errors.InvalidArgumentError),
    (4, errors.DeadlineExceededError),
    (5, errors.NotFoundError),
    (6, errors.AlreadyExistsError),
    (7, errors.PermissionDeniedError),
    (16, errors.UnauthenticatedError),
    (8, errors.ResourceExhaustedError),
    (9, errors.FailedPreconditionError),
    (10, errors.AbortedError),
    (11, errors.OutOfRangeError),
    (12, errors.UnimplementedError),
    (13, errors.InternalError),
    (14, errors.UnavailableError),
    (15, errors.DataLossError),
]:
    with self.assertRaises(expected_exception) as error:
        _errors_test_helper.TestRaiseFromTFStatus(code)
    self.assertEqual(error.exception.experimental_payloads[b"key1"],
                     b"value1")
    self.assertEqual(error.exception.experimental_payloads[b"key2"],
                     b"value2")
