# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py
dataset = dataset_ops.Dataset.range(10).take_while(
    predicate=lambda x: x < 2).repeat(5)
self.assertDatasetProduces(dataset, np.tile([0, 1], 5))
