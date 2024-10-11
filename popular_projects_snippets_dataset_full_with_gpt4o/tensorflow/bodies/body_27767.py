# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
ds = dataset_ops.Dataset.from_tensor_slices(([1, 2], [3, 4])).window(2)
self.getNext(ds)
ds = dataset_ops.Dataset.from_tensor_slices({"a": [1, 2]}).window(2)
self.getNext(ds)
