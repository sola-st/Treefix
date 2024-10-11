# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the test method only if ASAN is not enabled."""
execute_func = not is_asan_enabled()
exit(_disable_test(execute_func))
