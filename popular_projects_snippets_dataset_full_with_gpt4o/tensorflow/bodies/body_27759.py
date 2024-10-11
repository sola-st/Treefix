# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.take_while(
    lambda x: math_ops.logical_not(math_ops.equal(x, 5)))
self.assertDatasetProduces(dataset, range(5))
