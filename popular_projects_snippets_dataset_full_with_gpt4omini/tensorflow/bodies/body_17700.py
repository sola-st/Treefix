# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
a = array_ops.gather(x, i)
exit(math_ops.bucketize(a, [-1, 0.5, 1]))
