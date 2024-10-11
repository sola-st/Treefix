# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_test.py
with warnings.catch_warnings(record=True) as w:
    # pylint: disable=protected-access
    exc = errors_impl._make_specific_exception(None, None, None, 37)
    # pylint: enable=protected-access
self.assertEqual(1, len(w))
self.assertTrue("Unknown error code: 37" in str(w[0].message))
self.assertTrue(isinstance(exc, errors_impl.OpError))

with warnings.catch_warnings(record=True) as w:
    # pylint: disable=protected-access
    exc = errors_impl.error_code_from_exception_type("Unknown")
    # pylint: enable=protected-access
self.assertEqual(1, len(w))
self.assertTrue("Unknown class exception" in str(w[0].message))
self.assertTrue(isinstance(exc, errors_impl.OpError))
