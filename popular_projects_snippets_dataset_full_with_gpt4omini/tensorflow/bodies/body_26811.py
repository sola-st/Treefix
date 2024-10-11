# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
reducer = grouping.Reducer(
    init_func=lambda _: 0,
    reduce_func=lambda x, y: x,
    finalize_func=lambda _: var)
exit(dataset_ops.Dataset.range(5).apply(
    grouping.group_by_reducer(lambda x: x % 2, reducer)))
