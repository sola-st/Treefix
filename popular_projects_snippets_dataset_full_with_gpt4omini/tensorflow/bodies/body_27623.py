# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
reducer = grouping.Reducer(
    init_func=lambda _: np.int64(0),
    reduce_func=lambda x, y: x + y,
    finalize_func=lambda x: x)

exit(dataset_ops.Dataset.from_tensor_slices(components).apply(
    grouping.group_by_reducer(lambda x: x % 5, reducer)))
