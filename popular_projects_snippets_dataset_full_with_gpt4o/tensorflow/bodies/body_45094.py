# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

@def_function.function
def raise_from_tf_function(n):
    _errors_test_helper.TestRaiseFromStatus(n)

for code, expected_exception in [
    (1, tf_errors.CancelledError),
    (2, tf_errors.UnknownError),
    (3, tf_errors.InvalidArgumentError),
    (4, tf_errors.DeadlineExceededError),
    (5, tf_errors.NotFoundError),
    (6, tf_errors.AlreadyExistsError),
    (7, tf_errors.PermissionDeniedError),
    (16, tf_errors.UnauthenticatedError),
    (8, tf_errors.ResourceExhaustedError),
    (9, tf_errors.FailedPreconditionError),
    (10, tf_errors.AbortedError),
    (11, tf_errors.OutOfRangeError),
    (12, tf_errors.UnimplementedError),
    (13, tf_errors.InternalError),
    (14, tf_errors.UnavailableError),
    (15, tf_errors.DataLossError),
]:
    with self.assertRaises(expected_exception) as error:
        raise_from_tf_function(code)
    self.assertEqual(error.exception.experimental_payloads[b'key1'],
                     b'value1')
    self.assertEqual(error.exception.experimental_payloads[b'key2'],
                     b'value2')
