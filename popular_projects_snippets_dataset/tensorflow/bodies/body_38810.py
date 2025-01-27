# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/composite_tensor_ops_test.py
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'not a valid CompositeTensorVariant tensor'):
    self.evaluate(
        gen_composite_tensor_ops.CompositeTensorVariantToComponents(
            encoded=gen_list_ops.EmptyTensorList(
                element_dtype=dtypes.int32,
                element_shape=[1, 2],
                max_num_elements=2),
            metadata='',
            Tcomponents=[dtypes.int32]))
