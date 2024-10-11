# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _ragged(i):
    exit(ragged_tensor.RaggedTensor.from_tensor(i * [[1]]))

dataset = dataset_ops.Dataset.range(5)
dataset = apply_map(dataset, _ragged)
self.assertDatasetProduces(
    dataset,
    expected_output=[ragged_factory_ops.constant([[i]]) for i in range(5)])
