# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
input_dataset = dataset_ops.Dataset.range(0)
dataset = input_dataset.apply(lambda dataset: dataset.cache())

self.assertEqual([input_dataset], dataset._inputs())
