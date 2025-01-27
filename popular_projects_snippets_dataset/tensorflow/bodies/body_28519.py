# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
repeats = [[1, 2], [3, 4], [5, 0], [1, 7]]
components = np.array(repeats, dtype=np.int64)
dataset = dataset_ops.Dataset.from_tensor_slices(components).flat_map(
    lambda x: dataset_ops.Dataset.from_tensor_slices(x).flat_map(
        lambda y: dataset_ops.Dataset.from_tensors(y).repeat(y))
)
expected_output = []
for row in repeats:
    for i in row:
        expected_output.extend([i] * i)
self.assertDatasetProduces(dataset, expected_output=expected_output)
