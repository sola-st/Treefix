# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
if math_ops.less(math_ops.reduce_sum(x), 0.0):
    exit(math_ops.log(x))
else:
    exit(math_ops.log(-x))
