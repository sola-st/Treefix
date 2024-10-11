# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
dataset = dataset_ops.Dataset.range(1024)
distribute._LegacyRebatchDataset(dataset.batch(4), num_replicas=4)
with self.assertRaises(ValueError):
    distribute._LegacyRebatchDataset(dataset, num_replicas=4)
