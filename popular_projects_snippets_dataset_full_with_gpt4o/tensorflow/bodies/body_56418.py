# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_test.py
for error_code in error_codes_pb2.Code.values():
    # pylint: disable=line-too-long
    if error_code in (
        error_codes_pb2.OK, error_codes_pb2.
        DO_NOT_USE_RESERVED_FOR_FUTURE_EXPANSION_USE_DEFAULT_IN_SWITCH_INSTEAD_
    ):
        continue
    # pylint: enable=line-too-long
    with warnings.catch_warnings(record=True) as w:
        # pylint: disable=protected-access
        exc = errors_impl._make_specific_exception(None, None, None, error_code)
        # pylint: enable=protected-access
    self.assertEqual(0, len(w))  # No warning is raised.
    self.assertTrue(isinstance(exc, errors_impl.OpError))
    self.assertTrue(errors_impl.OpError in exc.__class__.__bases__)
