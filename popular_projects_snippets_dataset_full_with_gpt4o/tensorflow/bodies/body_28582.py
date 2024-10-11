# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
components = (np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]),
              np.array([9.0, 10.0, 11.0, 12.0]))

repeat_dataset = (
    dataset_ops.Dataset.from_tensor_slices(components).repeat(0))
cache_dataset = repeat_dataset.cache()

self.assertDatasetProduces(cache_dataset, expected_output=[])
