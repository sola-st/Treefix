# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
exit((array_ops.reshape(x1, [-1]), array_ops.reshape(x1, [1, 3, 1, -1])))
