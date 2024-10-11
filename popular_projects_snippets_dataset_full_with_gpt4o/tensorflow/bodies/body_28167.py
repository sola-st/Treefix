# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
dataset = dataset_ops.Dataset.range(12).batch(4, drop_remainder=False)
rebatched_dataset = dataset_ops.rebatch(
    dataset, batch_sizes=[6], drop_remainder=drop_remainder)

expected_output = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
self.assertDatasetProduces(rebatched_dataset, expected_output)
