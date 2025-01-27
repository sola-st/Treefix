# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py

st = sparse_tensor.SparseTensorValue(
    indices=[[0, 0]], values=([42]), dense_shape=[1, 1])

with self.assertRaisesRegex(
    TypeError, r'`padded_batch` is only supported for '
    r'datasets that produce tensor elements but type spec of elements in '
    r'the input dataset is not a subclass of TensorSpec: '
    r'`SparseTensorSpec.*`\.$'):
    _ = dataset_ops.Dataset.from_tensors(st).repeat(10).padded_batch(10)
