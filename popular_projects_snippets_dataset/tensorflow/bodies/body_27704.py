# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
dataset = dataset_ops.Dataset.range(16).batch(2).batch(4)
self.assertEqual([[None, None]], _flat_shapes(dataset))

# Each element is a list of 4 elements where each element is a list of 2.
expected_output = [[[0, 1], [2, 3], [4, 5], [6, 7]],
                   [[8, 9], [10, 11], [12, 13], [14, 15]]]
self.assertDatasetProduces(dataset, expected_output)

rebatched_dataset = distribute._LegacyRebatchDataset(dataset, 2)
self.assertEqual([[None, None]], _flat_shapes(rebatched_dataset))
# Each element is a list of 2 elements where each element is a list of 2.
expected_output = [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]],
                   [[12, 13], [14, 15]]]
self.assertDatasetProduces(rebatched_dataset, expected_output)
