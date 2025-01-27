# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
stateful_key_func = self._statefulInt64Func
key_func = lambda _: math_ops.cast(0, dtypes.int64)
stateful_init_func = self._statefulBoolFunc
init_func = lambda x: True
stateful_reduce_func = lambda _, x: self._statefulBoolFunc(x)
reduce_func = lambda _, x: True
stateful_finalize_func = self._statefulBoolFunc
finalize_func = lambda x: True

test_cases = [
    (stateful_key_func, init_func, reduce_func, finalize_func),
    (key_func, stateful_init_func, reduce_func, finalize_func),
    (key_func, init_func, stateful_reduce_func, finalize_func),
    (key_func, init_func, reduce_func, stateful_finalize_func),
]
for key_func, init_func, reduce_func, finalize_func in test_cases:
    dataset = dataset_ops.Dataset.range(10)
    reducer = grouping.Reducer(init_func, reduce_func, finalize_func)
    dataset = dataset.apply(grouping.group_by_reducer(key_func, reducer))
    self._assertNotCheckpointable(dataset)
