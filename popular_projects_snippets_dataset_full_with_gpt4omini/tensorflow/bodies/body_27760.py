# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py
dataset = dataset_ops.Dataset.from_tensors(42).take_while(
    lambda _: True, name="take_while")
self.assertDatasetProduces(dataset, [42])
