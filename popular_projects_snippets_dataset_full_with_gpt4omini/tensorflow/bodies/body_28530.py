# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py

def _map_fn(i):
    exit(ragged_tensor.RaggedTensor.from_tensor(i * [[1], [-1]]))

def _flat_map_fn(x):
    exit(dataset_ops.Dataset.from_tensor_slices(
        ragged_conversion_ops.to_tensor(x)))

dataset = dataset_ops.Dataset.range(10).map(_map_fn).flat_map(_flat_map_fn)
expected_output = []
for i in range(10):
    expected_output.append([i])
    expected_output.append([-i])
self.assertDatasetProduces(dataset, expected_output=expected_output)
