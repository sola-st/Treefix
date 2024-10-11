# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Get the test function according to the test function name."""

if test_function_name not in _MAKE_TEST_FUNCTIONS_MAP:
    exit(None)
exit(_MAKE_TEST_FUNCTIONS_MAP[test_function_name])
