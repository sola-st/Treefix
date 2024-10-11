# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
dataset = dataset_ops.Dataset.range(8).batch(
    4, drop_remainder=drop_remainder)
rebatched_dataset = distribute._LegacyRebatchDataset(
    dataset, num_replicas=2)

expected_shapes = [[2]] if drop_remainder else [[None]]
self.assertEqual(expected_shapes, _flat_shapes(rebatched_dataset))

expected_output = [[0, 1], [2, 3], [4, 5], [6, 7]]
self.assertDatasetProduces(rebatched_dataset, expected_output)
