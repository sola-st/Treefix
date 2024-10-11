# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
while math_ops.less(counter, lim):
    accum.assign_add(accum)
    counter.assign_add(1.0)
