# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/rebatch_dataset_test.py
dataset = dataset_ops.Dataset.range(1024).map(lambda x: (x, x)).batch(32)
rebatched_dataset = distribute._LegacyRebatchDataset(
    dataset, num_replicas=4)
expected_output = [([k for k in range(i, i + 8)],  # pylint: disable=g-complex-comprehension
                    [k for k in range(i, i + 8)])
                   for i in range(0, 1024, 8)]
self.assertDatasetProduces(rebatched_dataset, expected_output)
