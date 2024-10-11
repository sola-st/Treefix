# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
exit(array_ops.slice(x1, begin=(0, 2 - i, i), size=(-1, 2, 1)))
