# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the test method only if MSAN is not enabled."""
execute_func = not is_msan_enabled()
exit(_disable_test(execute_func))
