# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
input1 = dataset_ops.Dataset.range(0)
input2 = dataset_ops.Dataset.range(1)
self.assertEqual([input1, input2], dataset_fn(input1, input2)._inputs())
