# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
indices = array_ops.constant([[0, 0], [1, 0], [1, 1]],
                             dtype=dtypes.int64)[0:2 + i]
values = array_ops.constant([0, 0, 1], dtype=dtypes.int32)[0:2 + i]
shape = [
    array_ops.constant([2], dtype=dtypes.int64),
    array_ops.expand_dims(1 + i, axis=0)
]
dense_shape = array_ops.concat(shape, axis=0)
exit(sparse_tensor.SparseTensor(
    indices=indices, values=values, dense_shape=dense_shape))
