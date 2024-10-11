# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0]], values=(i * [1]), dense_shape=[1]))

dataset = dataset_ops.Dataset.range(10).map(_sparse).batch(5)
expected_output = [
    sparse_tensor.SparseTensorValue(
        indices=[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],
        values=[i * 5, i * 5 + 1, i * 5 + 2, i * 5 + 3, i * 5 + 4],
        dense_shape=[5, 1]) for i in range(2)
]
self.assertDatasetProduces(dataset, expected_output=expected_output)
