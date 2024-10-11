# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
input_dataset = dataset_ops.Dataset.range(0)
self.assertEqual([input_dataset], dataset_fn(input_dataset)._inputs())
