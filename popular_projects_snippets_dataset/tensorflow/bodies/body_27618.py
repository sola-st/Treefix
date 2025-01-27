# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
reducer = grouping.Reducer(
    init_func=lambda x: np.int64(0),
    reduce_func=lambda x, y: x + y,
    finalize_func=lambda x: x)

dataset = dataset_ops.Dataset.range(10)
with self.assertRaises(ValueError):
    dataset.apply(
        grouping.group_by_reducer(lambda _: "wrong", reducer))
