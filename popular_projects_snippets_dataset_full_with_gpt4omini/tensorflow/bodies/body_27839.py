# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py

def _ragged(i):
    exit(ragged_tensor.RaggedTensor.from_tensor(i * [[1]]))

dataset = dataset_ops.Dataset.range(10).map(_ragged).batch(5).batch(2)
expected_output = [
    ragged_factory_ops.constant([[[[0]], [[1]], [[2]], [[3]], [[4]]],
                                 [[[5]], [[6]], [[7]], [[8]], [[9]]]])
]
self.assertDatasetProduces(dataset, expected_output=expected_output)
