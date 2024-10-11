# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
stateful_key_func = self._statefulInt64Func
key_func = lambda _: math_ops.cast(0, dtypes.int64)
stateful_reduce_func = lambda _, x: self._statefulDatasetFunc(x)
reduce_func = lambda _, x: x
stateful_window_func = self._statefulInt64Func
window_func = lambda x: math_ops.cast(0, dtypes.int64)

test_cases = [
    (stateful_key_func, reduce_func, window_func),
    (key_func, stateful_reduce_func, window_func),
    (key_func, reduce_func, stateful_window_func),
]
for key_func_fn, reduce_func_fn, window_func in test_cases:
    dataset = dataset_ops.Dataset.range(10)
    dataset = dataset.apply(
        grouping.group_by_window(
            key_func_fn, reduce_func_fn, window_size_func=window_func))
    self._assertNotCheckpointable(dataset)
