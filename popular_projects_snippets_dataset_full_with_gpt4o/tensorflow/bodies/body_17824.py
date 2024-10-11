# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 3, 3, 3])
x2 = array_ops.placeholder_with_default(x, shape=None)  # Has dynamic shape.

def loop_fn(i):
    outputs = []
    x_i = array_ops.gather(x, i)
    for y in [x, x2, x_i]:
        for axis in [0, 2, -1]:
            outputs.append(array_ops.gather(y, 2, axis=axis))
            outputs.append(
                array_ops.gather(y, math_ops.cast(2, dtypes.int64), axis=axis))
            outputs.append(
                array_ops.gather(y, 2, axis=math_ops.cast(axis, dtypes.int64)))
            outputs.append(
                array_ops.gather(y, math_ops.cast(i, dtypes.int64), axis=axis))
            outputs.append(array_ops.gather(y, [i], axis=axis))
            outputs.append(array_ops.gather(y, [i, 2], axis=axis))
            outputs.append(array_ops.gather(y, [[2, i], [i, 1]], axis=axis))

        outputs.append(array_ops.gather(y, [0, 1, 2], axis=1, batch_dims=1))
        outputs.append(array_ops.gather(y, [i, 1, 2], axis=2, batch_dims=1))
        outputs.append(array_ops.gather(y, [[2, i], [i, 1], [2, 1]],
                                        axis=-1, batch_dims=1))
        outputs.append(
            array_ops.gather(y, [[0, 1, 2]] * 3, axis=2, batch_dims=2))
        outputs.append(array_ops.gather(y, [0, 1, 2], axis=1, batch_dims=-1))
        outputs.append(
            array_ops.gather(y, [[0, 1, 2]] * 3, axis=2, batch_dims=-2))

    exit(outputs)

self._test_loop_fn(loop_fn, 3)
