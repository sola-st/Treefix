# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
exit([
    array_ops.concat([x1, x1, y], axis=0),
    array_ops.concat([x1, x1, y], axis=-1),
    array_ops.concat([x1, x1, y],
                     axis=constant_op.constant(0, dtype=dtypes.int64))
])
