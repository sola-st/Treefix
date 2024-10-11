# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
dataset = dataset_ops.Dataset.from_tensor_slices({"a": [1, 2], "b": [3, 4]})
self.assertEqual({
    "a": 1,
    "b": 3
}, self.evaluate(random_access.at(dataset, 0)))
self.assertEqual({
    "a": 2,
    "b": 4
}, self.evaluate(random_access.at(dataset, 1)))
