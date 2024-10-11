# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/len_test.py
num_elements = 10
ds = dataset_ops.Dataset.range(num_elements)
self.assertLen(ds, 10)
