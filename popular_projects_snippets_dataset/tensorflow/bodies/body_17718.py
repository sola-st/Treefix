# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
exit(math_ops.tanh(a * array_ops.gather(x, i) + array_ops.gather(y, i)))
