# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
deprecated_func = deprecation.deprecated_alias("deprecated.func",
                                               "real.func",
                                               logging.error)

logging.error("fake error logged")
self.assertEqual(0, mock_warning.call_count)
deprecated_func("FAKE ERROR!")
self.assertEqual(1, mock_warning.call_count)
# Make sure the error points to the right file.
self.assertRegex(mock_warning.call_args[0][1], r"deprecation_test\.py:")
deprecated_func("ANOTHER FAKE ERROR!")
self.assertEqual(1, mock_warning.call_count)
