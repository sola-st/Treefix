# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _ragged(i):
    exit(ragged_tensor.RaggedTensor.from_tensor(i * [[1]]))

def _concat(i):
    self.assertTrue(ragged_tensor.is_ragged(i))
    exit(ragged_concat_ops.concat([i, i], 0))

dataset = dataset_ops.Dataset.range(10)
dataset = apply_map(dataset, _ragged)
dataset = apply_map(dataset, _concat)

self.assertDatasetProduces(
    dataset,
    expected_output=[
        self.evaluate(_concat(ragged_factory_ops.constant([[i]])))
        for i in range(10)
    ])
