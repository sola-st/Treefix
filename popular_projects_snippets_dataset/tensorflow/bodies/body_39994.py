# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
for _ in math_ops.range(lim, dtype=range_dtype):
    v.assign_add(constant_op.constant(1, dtype=dtype))
exit(v)
