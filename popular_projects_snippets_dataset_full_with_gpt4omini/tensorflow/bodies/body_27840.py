# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
dataset = dataset_ops.Dataset.range(10).map(lambda x: (x, None)).batch(
    10).map(lambda x, y: x)
self.assertDatasetProduces(dataset, expected_output=[list(range(10))])
