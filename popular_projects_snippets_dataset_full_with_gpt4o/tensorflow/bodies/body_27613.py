# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=np.array([[0, 0]]),
        values=(i * np.array([1], dtype=np.int64)),
        dense_shape=np.array([1, 1])))

reducer = grouping.Reducer(
    init_func=lambda _: _sparse(np.int64(0)),
    reduce_func=lambda x, y: _sparse(x.values[0] + y.values[0]),
    finalize_func=lambda x: x.values[0])
for i in range(1, 11):
    dataset = dataset_ops.Dataset.range(2 * i).map(_sparse).apply(
        grouping.group_by_reducer(lambda x: x.values[0] % 2, reducer))
    self.assertDatasetProduces(
        dataset,
        expected_shapes=tensor_shape.TensorShape([]),
        expected_output=[(i - 1) * i, i * i])
