# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
st = sparse_tensor.SparseTensorValue(
    indices=[[i, i] for i in range(10)],
    values=list(range(10)),
    dense_shape=[10, 10])
data = dataset_ops.Dataset.from_tensors(st)
data = data.unbatch()
data = data.batch(5)
data = data.unbatch()
expected_output = [
    sparse_tensor.SparseTensorValue([[i]], [i], [10]) for i in range(10)
]
self.assertDatasetProduces(data, expected_output=expected_output)
