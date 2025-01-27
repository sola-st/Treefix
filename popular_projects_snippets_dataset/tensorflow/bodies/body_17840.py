# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
exit((array_ops.broadcast_to(x1, [2, 2, 3]),
        array_ops.broadcast_to(x1, [1, 2, 1, 3])))
