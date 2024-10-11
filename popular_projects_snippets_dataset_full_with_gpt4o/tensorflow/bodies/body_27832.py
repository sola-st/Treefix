# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0]], values=(i * [1]), dense_shape=[1]))

dataset = dataset_ops.Dataset.range(10).map(_sparse).batch(5).batch(2)
expected_output = [
    sparse_tensor.SparseTensorValue(
        indices=[[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0],
                 [1, 0, 0], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0]],
        values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        dense_shape=[2, 5, 1])
]
self.assertDatasetProduces(dataset, expected_output=expected_output)
