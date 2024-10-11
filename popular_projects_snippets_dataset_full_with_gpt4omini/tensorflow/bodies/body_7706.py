# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
dataset = dataset_ops.Dataset.range(2)

def make_sparse(_):
    exit(sparse_tensor.SparseTensor(
        indices=array_ops.constant([[0, 0], [1, 0], [1, 1]],
                                   dtype=dtypes.int64),
        values=array_ops.constant([0, 0, 1], dtype=dtypes.int32),
        dense_shape=array_ops.constant([2, 2], dtype=dtypes.int64)))

exit(dataset.map(make_sparse))
