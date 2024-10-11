# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
indices_i = array_ops.gather(indices, i)
exit((array_ops.one_hot(indices_i, depth=4, on_value=2., off_value=-2.),
        array_ops.one_hot(indices_i, depth=4, axis=1)))
