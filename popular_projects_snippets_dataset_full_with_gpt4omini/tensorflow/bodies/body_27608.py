# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
reducer = grouping.Reducer(
    init_func=lambda _: np.int64(0),
    reduce_func=lambda x, y: x + y,
    finalize_func=lambda x: x)
for i in range(1, 11):
    dataset = dataset_ops.Dataset.range(2 * i).apply(
        grouping.group_by_reducer(lambda x: x % 2, reducer))
    self.assertDatasetProduces(
        dataset,
        expected_shapes=tensor_shape.TensorShape([]),
        expected_output=[(i - 1) * i, i * i])
