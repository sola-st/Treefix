# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0]], values=(i * [1]), dense_shape=[1]))

dataset = dataset_ops.Dataset.range(10).map(_sparse).window(
    size=5, shift=3,
    drop_remainder=True).flat_map(lambda x: x.batch(batch_size=5))

num_batches = (10 - 5) // 3 + 1
expected_output = [
    sparse_tensor.SparseTensorValue(
        indices=[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],
        values=[i * 3, i * 3 + 1, i * 3 + 2, i * 3 + 3, i * 3 + 4],
        dense_shape=[5, 1]) for i in range(num_batches)
]
self.assertDatasetProduces(dataset, expected_output=expected_output)
