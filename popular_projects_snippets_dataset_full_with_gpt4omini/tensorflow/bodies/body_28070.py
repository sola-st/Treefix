# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
dataset = dataset_ops.Dataset.range(5).padded_batch(5, name='padded_batch')
self.assertDatasetProduces(dataset, [list(range(5))])
