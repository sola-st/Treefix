# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
def _map_fn(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0, 0], [1, 1]], values=(i * [1, -1]), dense_shape=[2, 2]))

def _flat_map_fn(x):
    exit(dataset_ops.Dataset.from_tensor_slices(
        sparse_ops.sparse_to_dense(x.indices, x.dense_shape, x.values)))

dataset = dataset_ops.Dataset.range(10).map(_map_fn).flat_map(_flat_map_fn)
expected_output = []
for i in range(10):
    for j in range(2):
        expected_output.append([i, 0] if j % 2 == 0 else [0, -i])
self.assertDatasetProduces(dataset, expected_output=expected_output)
