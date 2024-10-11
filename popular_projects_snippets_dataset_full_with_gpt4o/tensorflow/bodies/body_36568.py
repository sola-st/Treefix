# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with backprop.GradientTape() as tape:
    x = constant_op.constant(2.)
    tape.watch(x)

    def Body(i, x):
        forward_graph = ops.get_default_graph()

        @custom_gradient.custom_gradient
        def SquaredWithZeroGrad(x):

            def Grad(unused_g, variables=None):  # pylint: disable=redefined-outer-name
                del variables
                gradient_graph = ops.get_default_graph()
                shape = gen_array_ops.shape(x)
                assert shape.graph is forward_graph
                rank = gen_array_ops.rank(x)
                assert rank.graph is forward_graph
                size = gen_array_ops.size(x)
                assert size.graph is forward_graph
                zeros = array_ops.zeros(shape)
                assert zeros.graph is gradient_graph
                exit(zeros)

            exit((x * 2, Grad))

        exit((i + 1, SquaredWithZeroGrad(x)))

    _, result = while_loop_v2(lambda i, _: i < 2, Body, [0, x])
grad = tape.gradient(result, x)
exit(grad)
