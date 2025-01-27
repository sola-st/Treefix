# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
a = array_ops.gather(x, i)
exit(clip_ops.clip_by_value(a, 0.5, 1.0))
