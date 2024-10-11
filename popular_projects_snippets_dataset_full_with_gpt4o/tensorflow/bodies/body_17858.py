# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x_i = array_ops.gather(x, i)
exit((array_ops.unstack(
    x_i, 4, axis=-1), array_ops.unstack(
        x_i, 3, axis=1)))
