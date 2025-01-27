# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
exit((array_ops.squeeze(x1, axis=0), array_ops.squeeze(x1, axis=-1),
        array_ops.squeeze(x1)))
