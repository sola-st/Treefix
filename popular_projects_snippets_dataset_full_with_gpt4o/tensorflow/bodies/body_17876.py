# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
z = array_ops.zeros_like(x1),
exit((z, z + x1))
