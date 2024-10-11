# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=np.array([[0, 0]]),
        values=(i * np.array([1])),
        dense_shape=np.array([1, 1])))

def _build_ds(num_outputs):
    exit(dataset_ops.Dataset.range(num_outputs).map(
        _sparse, num_parallel_calls=num_parallel_calls))

num_outputs = 10
verify_fn(self, lambda: _build_ds(num_outputs), num_outputs=num_outputs)
