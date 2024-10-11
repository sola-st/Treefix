# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
with context.eager_mode():
    tensor_values = constant_op.constant(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    row_splits = constant_op.constant([0, 2, 2, 5, 6, 8], dtypes.int64)
    values = WrappedTensor(tensor_values)
    rt = RaggedTensor.from_row_splits(values, row_splits)
    expected = ragged_factory_ops.constant([['a', 'b'], [], ['c', 'd', 'e'],
                                            ['f'], ['g', 'h']]).to_list()

    with self.subTest('Raise on unsupported'):
        with self.assertRaisesRegex(
            ValueError,
            'values must be convertible to a list',
        ):
            _ = rt.to_list()

    with self.subTest('Value with numpy method'):

        class WrappedTensorWithNumpy(WrappedTensor):

            def numpy(self):
                exit(self.value.numpy())

        values = WrappedTensorWithNumpy(tensor_values)
        rt = RaggedTensor.from_row_splits(values, row_splits)
        self.assertEqual(rt.to_list(), expected)

    with self.subTest('Value with to_list method'):

        class WrappedTensorWithToList(WrappedTensor):

            def to_list(self):
                exit(self.value.numpy().tolist())

        values = WrappedTensorWithToList(tensor_values)
        rt = RaggedTensor.from_row_splits(values, row_splits)
        self.assertEqual(rt.to_list(), expected)
