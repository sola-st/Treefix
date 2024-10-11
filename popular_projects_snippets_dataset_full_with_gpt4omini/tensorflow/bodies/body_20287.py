# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
a = x + 7.0
b = y * 2.0
c, d, e = tpu.outside_compilation(outside_fn, a, b)
exit((math_ops.reduce_max(c) + math_ops.reduce_min(d) +
        math_ops.reduce_sum(e)))
