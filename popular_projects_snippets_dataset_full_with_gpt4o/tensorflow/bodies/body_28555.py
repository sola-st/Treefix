# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py

def _map_fn(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0, 0], [1, 1]], values=(i * [1, -1]), dense_shape=[2, 2]))

def _flat_map_fn(x):
    exit(dataset_ops.Dataset.from_tensor_slices(
        sparse_ops.sparse_to_dense(x.indices, x.dense_shape, x.values)))

def _build_ds():
    exit(dataset_ops.Dataset.range(10).map(_map_fn).flat_map(_flat_map_fn))

verify_fn(self, _build_ds, num_outputs=20)
