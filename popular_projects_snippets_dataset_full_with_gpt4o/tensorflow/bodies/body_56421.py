# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_test.py
for error_code in [
    errors.CANCELLED,
    errors.UNKNOWN,
    errors.INVALID_ARGUMENT,
    errors.DEADLINE_EXCEEDED,
    errors.NOT_FOUND,
    errors.ALREADY_EXISTS,
    errors.PERMISSION_DENIED,
    errors.UNAUTHENTICATED,
    errors.RESOURCE_EXHAUSTED,
    errors.FAILED_PRECONDITION,
    errors.ABORTED,
    errors.OUT_OF_RANGE,
    errors.UNIMPLEMENTED,
    errors.INTERNAL,
    errors.UNAVAILABLE,
    errors.DATA_LOSS,
]:
    # pylint: disable=protected-access
    exc = errors_impl._make_specific_exception(None, None, None, error_code)
    # pylint: enable=protected-access
    unpickled = pickle.loads(pickle.dumps(exc))
    self.assertEqual(exc.node_def, unpickled.node_def)
    self.assertEqual(exc.op, unpickled.op)
    self.assertEqual(exc.message, unpickled.message)
    self.assertEqual(exc.error_code, unpickled.error_code)
