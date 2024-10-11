# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
with forwardprop.ForwardAccumulator(y, 1.) as acc:
    ret = 0.
    for i in math_ops.range(iters):
        ret += y * math_ops.cast(i, dtypes.float32)
exit(acc.jvp(ret))
