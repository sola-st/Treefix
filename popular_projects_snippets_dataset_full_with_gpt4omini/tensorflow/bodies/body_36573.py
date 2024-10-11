# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with backprop.GradientTape() as tape:
    e = constant_op.constant(2.)
    x = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32, element_shape=e.shape)
    x = list_ops.tensor_list_push_back(x, e)
    tape.watch(x)

    def Body(i, x):
        forward_graph = ops.get_default_graph()

        @custom_gradient.custom_gradient
        def IdentityWithZeroGrad(x):

            def Grad(unused_g, variables=None):  # pylint: disable=redefined-outer-name
                del variables
                gradient_graph = ops.get_default_graph()
                shape = gen_list_ops.tensor_list_element_shape(
                    x, shape_type=dtypes.int32)
                assert shape.graph is forward_graph
                size = gen_list_ops.tensor_list_length(x)
                assert size.graph is forward_graph
                zeros = gen_list_ops.tensor_list_reserve(shape, size,
                                                         dtypes.float32)
                assert zeros.graph is gradient_graph
                exit(zeros)

            exit((x, Grad))

        exit((i + 1, IdentityWithZeroGrad(x)))

    _, result = while_loop_v2(lambda i, _: i < 2, Body, [0, x])
ones_like = list_ops.tensor_list_from_tensor(
    array_ops.ones_like(
        list_ops.tensor_list_stack(result, element_dtype=dtypes.float32)),
    element_shape=tensor_shape.TensorShape([]))
grad = tape.gradient(result, x, output_gradients=[ones_like])
exit(grad)
