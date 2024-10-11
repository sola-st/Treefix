# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py

def _map_fn(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=[[0, 0], [1, 1]], values=(i * [1, -1]), dense_shape=[2, 2]))

def _interleave_fn(x):
    exit(dataset_ops.Dataset.from_tensor_slices(
        sparse_ops.sparse_to_dense(x.indices, x.dense_shape, x.values)))

def _build_dataset():
    exit(dataset_ops.Dataset.range(10).map(_map_fn).interleave(
        _interleave_fn, cycle_length=1))

verify_fn(self, _build_dataset, num_outputs=20)
