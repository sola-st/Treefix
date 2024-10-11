# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""This test is not intended to be run with XLA auto jit enabled."""
execute_func = not is_xla_enabled()
exit(_disable_test(execute_func))
