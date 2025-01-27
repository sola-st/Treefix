# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
st = sparse_tensor.SparseTensorValue(
    indices=[[i, i] for i in range(10)],
    values=list(range(10)),
    dense_shape=[10, 10])
rt = ragged_factory_ops.constant_value([[[0]], [[1]], [[2]], [[3]], [[4]],
                                        [[5]], [[6]], [[7]], [[8]], [[9]]])
data = dataset_ops.Dataset.from_tensors((list(range(10)), st, rt))
data = data.unbatch()
data = data.batch(5)
data = data.unbatch()
expected_output = [(i, sparse_tensor.SparseTensorValue([[i]], [i], [10]),
                    ragged_factory_ops.constant_value([[i]]))
                   for i in range(10)]
self.assertDatasetProduces(
    data, expected_output=expected_output)
