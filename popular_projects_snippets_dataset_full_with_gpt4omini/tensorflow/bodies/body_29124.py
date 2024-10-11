# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
dataset = dataset_ops.Dataset.from_tensors(
    (list(range(10)), None)).unbatch().map(lambda x, y: x)
self.assertDatasetProduces(dataset, expected_output=range(10))
