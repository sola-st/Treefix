# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py

def map_fn(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0]], values=(i * [1]), dense_shape=[1]))

exit(dataset_ops.Dataset.range(10).apply(
    batching.map_and_batch(map_fn, 5)))
