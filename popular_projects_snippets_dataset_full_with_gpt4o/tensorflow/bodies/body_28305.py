# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensors(21).map(
    lambda x: x * 2, num_parallel_calls=num_parallel_calls, name="map")
self.assertDatasetProduces(dataset, [42])
