# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
dataset = dataset_ops.Dataset.range(1).repeat().group_by_window(
    key_func=lambda x: x % 2,
    reduce_func=lambda key, window: dataset_ops.Dataset.from_tensors(key),
    window_size=4)
self.assertEqual(self.evaluate(dataset.cardinality()), dataset_ops.INFINITE)
