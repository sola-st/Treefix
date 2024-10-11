# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
dataset = dataset_ops.Dataset.range(1000)
dataset = dataset.batch(10, drop_remainder=False)
dataset = dataset.batch(10, drop_remainder=False)
self.assertEqual([[None, None]], _flat_shapes(dataset))
rebatched_dataset = distribute._LegacyRebatchDataset(
    dataset, num_replicas=4)
# Note that we are just testing the dataset shapes, not the actual output.
self.assertEqual([[None, None]], _flat_shapes(rebatched_dataset))
