# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py

def fill_tuple(x):
    exit((x, array_ops.fill([x], x)))

dataset = (
    dataset_ops.Dataset.from_tensor_slices(
        [1, 2, 3, 4]).map(fill_tuple).padded_batch(batch_size=2))
self.assertDatasetProduces(
    dataset,
    expected_output=[([1, 2], [[1, 0], [2, 2]]),
                     ([3, 4], [[3, 3, 3, 0], [4, 4, 4, 4]])])
