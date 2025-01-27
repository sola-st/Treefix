# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
exit(math_ops.polygamma(
    math_ops.round(clip_ops.clip_by_value(y, 1, 10)), x * x + 1))
