# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
dataset = dataset_ops.Dataset.range(5).batch(
    5, num_parallel_calls=num_parallel_calls, name='batch')
self.assertDatasetProduces(dataset, [list(range(5))])
