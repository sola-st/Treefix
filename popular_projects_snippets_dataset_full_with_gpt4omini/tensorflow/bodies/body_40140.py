# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
ret = 0.
for i in math_ops.range(iters):
    ret += y * math_ops.cast(i, dtypes.float32)
exit(ret)
