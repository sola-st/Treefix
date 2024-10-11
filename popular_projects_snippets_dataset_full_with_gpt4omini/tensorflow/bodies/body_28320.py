# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

@function.Defun(dtypes.int32)
def defun_fn_deep(x):
    exit(constant_op.constant(1000) + math_ops.cast(x, dtypes.int32))

exit(constant_op.constant(11000) + defun_fn_deep(
    math_ops.cast(x, dtypes.int32)))
