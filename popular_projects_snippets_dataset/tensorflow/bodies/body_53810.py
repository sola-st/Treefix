# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the test method only if UBSAN is not enabled."""
execute_func = not is_ubsan_enabled()
exit(_disable_test(execute_func))
