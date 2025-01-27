# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
dataset = dataset_ops.Dataset.range(8).batch(
    4, drop_remainder=drop_remainder)
rebatched_dataset = distribute._LegacyRebatchDataset(
    dataset, num_replicas=3)
self.assertEqual([[None]], _flat_shapes(rebatched_dataset))
# This rebatches into sub-batches of size 2, since ceil(4 / 3) = 2. However,
# this means that only the first 2 replicas will get data.
expected_output = [[0, 1], [2, 3], [], [4, 5], [6, 7], []]
self.assertDatasetProduces(rebatched_dataset, expected_output)
