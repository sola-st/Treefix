# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
exit([
    array_ops.expand_dims(x1, axis=-1),
    array_ops.expand_dims(x1, axis=1),
    array_ops.expand_dims(
        x1, axis=constant_op.constant(1, dtype=dtypes.int64))
])
