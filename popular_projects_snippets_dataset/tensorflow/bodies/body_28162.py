# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rebatch_test.py
dataset = dataset_ops.Dataset.range(10).batch(5, drop_remainder=True)
rebatched_dataset = dataset_ops.rebatch(
    dataset, batch_sizes=[2, 2], drop_remainder=False)
expected_shapes = [[None]]
self.assertEqual(expected_shapes, _flat_shapes(rebatched_dataset))
