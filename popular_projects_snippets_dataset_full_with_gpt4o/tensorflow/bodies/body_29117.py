# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
rt = ragged_factory_ops.constant_value([[[0]], [[1]], [[2]], [[3]], [[4]],
                                        [[5]], [[6]], [[7]], [[8]], [[9]]])
data = dataset_ops.Dataset.from_tensors(rt)
data = data.unbatch()
data = data.batch(5)
data = data.batch(2)
data = data.unbatch()
expected_output = [
    ragged_factory_ops.constant_value([[[0]], [[1]], [[2]], [[3]], [[4]]]),
    ragged_factory_ops.constant_value([[[5]], [[6]], [[7]], [[8]], [[9]]]),
]
self.assertDatasetProduces(
    data, expected_output=expected_output)
