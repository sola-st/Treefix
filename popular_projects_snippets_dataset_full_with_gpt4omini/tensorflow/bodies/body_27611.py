# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
components = np.array(list("abcdefghijklmnopqrst")).view(np.chararray)
reducer = grouping.Reducer(
    init_func=lambda x: "",
    reduce_func=lambda x, y: x + y[0],
    finalize_func=lambda x: x)
for i in range(1, 11):
    dataset = dataset_ops.Dataset.zip(
        (dataset_ops.Dataset.from_tensor_slices(components),
         dataset_ops.Dataset.range(2 * i))).apply(
             grouping.group_by_reducer(lambda x, y: y % 2, reducer))
    self.assertDatasetProduces(
        dataset,
        expected_shapes=tensor_shape.TensorShape([]),
        expected_output=[b"acegikmoqs"[:i], b"bdfhjlnprt"[:i]])
