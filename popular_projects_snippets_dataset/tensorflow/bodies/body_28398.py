# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
components = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0], dtype=np.int64)
dataset = dataset_ops.Dataset.from_tensor_slices(components)
dataset = dataset.group_by_window(
    key_func=lambda x: x % 2,
    reduce_func=lambda _, xs: xs.batch(4),
    window_size=4)
get_next = self.getNext(dataset)
self.assertAllEqual([0, 0, 0, 0], self.evaluate(get_next()))
self.assertAllEqual([1, 1, 1, 1], self.evaluate(get_next()))
# The small outputs at the end are deterministically produced in key
# order.
self.assertAllEqual([0, 0, 0], self.evaluate(get_next()))
self.assertAllEqual([1], self.evaluate(get_next()))
