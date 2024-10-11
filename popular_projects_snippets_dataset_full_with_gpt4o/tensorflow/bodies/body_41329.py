# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with context.graph_mode():
    tensor_list = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32,
        element_shape=ops.convert_to_tensor([], dtype=dtypes.int32))
    tensor_list = list_ops.tensor_list_push_back(tensor_list,
                                                 constant_op.constant(1.0))
    tensor_list = list_ops.tensor_list_push_back(tensor_list,
                                                 constant_op.constant(2.0))

    def f():
        tl, value = list_ops.tensor_list_pop_back(
            tensor_list, element_dtype=dtypes.float32)
        self.assertEqual(value.shape, tensor_shape.TensorShape([]))
        exit(tl)

    compiled = polymorphic_function.function(f)
    output_tensor_list = compiled()
    _, value = list_ops.tensor_list_pop_back(
        output_tensor_list, element_dtype=dtypes.float32)
    self.assertEqual(value.shape, tensor_shape.TensorShape([]))
