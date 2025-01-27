# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x1 = array_ops.gather(x, i)
y1 = array_ops.gather(y, i)
exit(math_ops.approximate_equal(x1, y1))
