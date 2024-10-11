# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
exit((array_ops.split(x1, 2, axis=0), array_ops.split(x1, 3, axis=-1)))
