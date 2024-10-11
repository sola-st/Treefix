# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.map(lambda x: x**2)
dataset = dataset.filter(lambda x: x > 10)
debug_string = dataset.__debug_string__()
for transformation in ["Range", "Map", "Filter"]:
    self.assertContainsSubsequence(debug_string, transformation)
