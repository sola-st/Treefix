# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
if math_ops.equal(x, 0):
    exit(script_ops.py_func(sleep, [x], x.dtype, stateful=False))
else:
    exit(x)
