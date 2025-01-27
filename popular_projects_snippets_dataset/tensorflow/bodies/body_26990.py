# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0]], values=(i * [1]), dense_shape=[1]))

dataset = dataset_ops.Dataset.range(10).apply(
    batching.map_and_batch(_sparse, 5))

self.assertDatasetProduces(
    dataset,
    expected_output=[
        sparse_tensor.SparseTensorValue(
            indices=[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],
            values=[i * 5, i * 5 + 1, i * 5 + 2, i * 5 + 3, i * 5 + 4],
            dense_shape=[5, 1]) for i in range(2)
    ])
