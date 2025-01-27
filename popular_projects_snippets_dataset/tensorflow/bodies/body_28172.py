# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
dataset = dataset_ops.Dataset.range(16).batch(
    2, drop_remainder=True).batch(
        4, drop_remainder=True)
self.assertEqual([[4, 2]], _flat_shapes(dataset))

rebatched_dataset = dataset_ops.rebatch(dataset, [2, 2])
self.assertEqual([[2, 2]], _flat_shapes(rebatched_dataset))
# Each element is a list of 2 elements where each element is a list of 2.
expected_output = [[[0, 1], [2, 3]], [[4, 5], [6, 7]], [[8, 9], [10, 11]],
                   [[12, 13], [14, 15]]]
self.assertDatasetProduces(rebatched_dataset, expected_output)
