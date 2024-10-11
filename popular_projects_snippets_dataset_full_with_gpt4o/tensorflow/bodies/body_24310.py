# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
while math_ops.less(counter, lim):
    accum.assign(accum * 2.0)
    counter.assign_add(1)
