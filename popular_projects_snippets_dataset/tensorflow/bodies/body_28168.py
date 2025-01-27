# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
# It's possible for splits to be empty if the batch size is smaller than
# the number of replicas. Here, we use an example with batch_size == 4
# and num_replicas == 5.
dataset = dataset_ops.Dataset.range(8).batch(4, drop_remainder=True)
rebatched_dataset = dataset_ops.rebatch(
    dataset, batch_sizes=[1, 1, 1, 1, 0], drop_remainder=drop_remainder)

expected_shapes = [[None]]
self.assertEqual(expected_shapes, _flat_shapes(rebatched_dataset))

expected_output = [[0], [1], [2], [3], [], [4], [5], [6], [7], []]
self.assertDatasetProduces(rebatched_dataset, expected_output)
