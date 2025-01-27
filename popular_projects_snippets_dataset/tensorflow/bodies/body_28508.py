# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
dataset = dataset_ops.Dataset.from_tensors(42).shuffle(1, name="shuffle")
self.assertDatasetProduces(dataset, [42])
