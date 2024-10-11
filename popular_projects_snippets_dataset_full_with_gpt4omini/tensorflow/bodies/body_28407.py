# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
dataset = dataset_ops.Dataset.from_tensors(np.int64(42)).group_by_window(
    key_func=lambda x: x,
    reduce_func=lambda key, window: window.batch(4),
    window_size=4,
    name="group_by_window")
self.assertDatasetProduces(dataset, [[42]])
