# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
dataset = dataset_ops.Dataset.range(4).group_by_window(
    key_func=lambda _: 0, reduce_func=lambda _, xs: xs, window_size=0)
get_next = self.getNext(dataset)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Window size must be greater than zero, but got 0."):
    print(self.evaluate(get_next()))
