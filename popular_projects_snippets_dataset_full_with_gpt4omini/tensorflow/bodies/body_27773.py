# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0]], values=(i * [1]), dense_shape=[1]))

dataset = dataset_ops.Dataset.range(10).map(_sparse).window(
    size=4, shift=2,
    drop_remainder=True).flat_map(lambda x: x.batch(batch_size=4)).window(
        size=3, shift=1,
        drop_remainder=True).flat_map(lambda x: x.batch(batch_size=3))

expected_output = [
    sparse_tensor.SparseTensorValue(
        indices=[[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [1, 0, 0],
                 [1, 1, 0], [1, 2, 0], [1, 3, 0], [2, 0, 0], [2, 1, 0],
                 [2, 2, 0], [2, 3, 0]],
        values=[0, 1, 2, 3, 2, 3, 4, 5, 4, 5, 6, 7],
        dense_shape=[3, 4, 1]),
    sparse_tensor.SparseTensorValue(
        indices=[[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [1, 0, 0],
                 [1, 1, 0], [1, 2, 0], [1, 3, 0], [2, 0, 0], [2, 1, 0],
                 [2, 2, 0], [2, 3, 0]],
        values=[2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9],
        dense_shape=[3, 4, 1])
]
self.assertDatasetProduces(dataset, expected_output=expected_output)
