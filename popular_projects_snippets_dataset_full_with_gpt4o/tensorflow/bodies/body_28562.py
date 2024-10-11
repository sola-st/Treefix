# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
a = dataset_ops.Dataset.range(5)
b = dataset_ops.Dataset.range(5, 10)
c = a.concatenate(b, name="concatenate")
self.assertDatasetProduces(c, list(range(10)))
