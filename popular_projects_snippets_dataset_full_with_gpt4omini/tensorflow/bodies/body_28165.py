# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
dataset = dataset_ops.Dataset.range(5).batch(4, drop_remainder=False)
rebatched_dataset = dataset_ops.rebatch(
    dataset, batch_sizes=[2, 2], drop_remainder=False)

expected_shapes = [[None]]
self.assertEqual(expected_shapes, _flat_shapes(rebatched_dataset))
expected_output = [[0, 1], [2, 3], [4]]
self.assertDatasetProduces(rebatched_dataset, expected_output)
