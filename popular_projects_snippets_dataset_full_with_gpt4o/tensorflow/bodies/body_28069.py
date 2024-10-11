# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py

def fill(x):
    exit(array_ops.fill([x], x))

dataset = dataset_ops.Dataset.zip(
    (dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4]).map(fill),
     dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4]).map(fill)))
dataset = dataset.padded_batch(batch_size=2, padding_values=-1)
self.assertDatasetProduces(
    dataset,
    expected_output=[([[1, -1], [2, 2]], [[1, -1], [2, 2]]),
                     ([[3, 3, 3, -1], [4, 4, 4, 4]], [[3, 3, 3, -1],
                                                      [4, 4, 4, 4]])])
