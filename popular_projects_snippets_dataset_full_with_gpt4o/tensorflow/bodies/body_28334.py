# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/prefetch_test.py
dataset = dataset_ops.Dataset.range(100)
dataset = prefetch_op._PrefetchDataset(  # pylint: disable=protected-access
    dataset, buffer_size, slack_period=slack_period)
self.assertDatasetProduces(dataset, expected_output=range(100))
