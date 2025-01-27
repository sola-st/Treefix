# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 2, 3])
y = random_ops.random_uniform([2, 3])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit([
        array_ops.concat([x1, x1, y], axis=0),
        array_ops.concat([x1, x1, y], axis=-1),
        array_ops.concat([x1, x1, y],
                         axis=constant_op.constant(0, dtype=dtypes.int64))
    ])

self._test_loop_fn(loop_fn, 3)
