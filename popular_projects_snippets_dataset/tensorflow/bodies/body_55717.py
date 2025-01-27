# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
self.assertFalse(
    error_interpolation._is_framework_filename(
        error_interpolation._FRAMEWORK_PATH_PREFIXES[0] + "foobar_test.py"))
