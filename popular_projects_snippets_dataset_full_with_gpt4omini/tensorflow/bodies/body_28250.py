# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=np.array([[0, 0]]),
        values=(i * np.array([1])),
        dense_shape=np.array([1, 1])))

dataset = dataset_ops.Dataset.range(10)
dataset = apply_map(dataset, _sparse)
self.assertDatasetProduces(
    dataset, expected_output=[_sparse(i) for i in range(10)])
