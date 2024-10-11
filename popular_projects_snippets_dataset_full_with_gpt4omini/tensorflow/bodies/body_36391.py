# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
# Upon exiting this function, the py_func holds the sole reference
# to this lambda, without which it would be garbage collected.
exit(script_ops.py_func(lambda x: x, [x], [dtypes.float32]))
