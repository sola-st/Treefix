# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
components = np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 0, 0, 2, 2, 0, 0],
                      dtype=np.int64)
dataset = dataset_ops.Dataset.from_tensor_slices(components)
dataset = dataset.repeat(-1)
dataset = dataset.group_by_window(
    key_func=lambda x: x % 3,
    reduce_func=lambda _, xs: xs.batch(4),
    window_size=4)
get_next = self.getNext(dataset)
# The input is infinite, so this test demonstrates that:
# 1. We produce output without having to consume the entire input,
# 2. Different buckets can produce output at different rates, and
# 3. For deterministic input, the output is deterministic.
for _ in range(3):
    self.assertAllEqual([0, 0, 0, 0], self.evaluate(get_next()))
    self.assertAllEqual([1, 1, 1, 1], self.evaluate(get_next()))
    self.assertAllEqual([2, 2, 2, 2], self.evaluate(get_next()))
    self.assertAllEqual([0, 0, 0, 0], self.evaluate(get_next()))
