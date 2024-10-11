# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
x = dataset_ops.Dataset.from_tensors(4)
y = dataset_ops.Dataset.from_tensors(2)
dataset = dataset_ops.Dataset.zip((x, y), name="zip")
self.assertDatasetProduces(dataset, [(4, 2)])
