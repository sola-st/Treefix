# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
reducer = grouping.Reducer(
    init_func=lambda x: constant_op.constant(1, dtype=dtypes.int32),
    reduce_func=lambda x, y: constant_op.constant(1, dtype=dtypes.int64),
    finalize_func=lambda x: x)

dataset = dataset_ops.Dataset.range(10)
with self.assertRaises(TypeError):
    dataset.apply(
        grouping.group_by_reducer(lambda _: np.int64(0), reducer))
