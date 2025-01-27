# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
if math_ops.equal(x, 0):
    exit(script_ops.py_func(sleep, [x], x.dtype))
else:
    exit(x)
