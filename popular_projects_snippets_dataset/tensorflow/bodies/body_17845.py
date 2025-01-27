# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
indices = random_ops.random_uniform([3, 2, 3],
                                    minval=0,
                                    maxval=4,
                                    dtype=dtypes.int32)

def loop_fn(i):
    indices_i = array_ops.gather(indices, i)
    exit((array_ops.one_hot(indices_i, depth=4, on_value=2., off_value=-2.),
            array_ops.one_hot(indices_i, depth=4, axis=1)))

self._test_loop_fn(loop_fn, 3)
