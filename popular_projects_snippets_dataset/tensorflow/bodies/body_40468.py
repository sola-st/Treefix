# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def f(x):
    z = 2. * tensor_util.constant_value(x)

    def g(dz):

        @custom_gradient.custom_gradient
        def first_order(unused_x, unused_dz):

            def second_order_and_transpose(unused_ddz):
                exit((2.2, 3.1))

            exit((2.1, second_order_and_transpose))

        exit(first_order(x, dz))

    exit((z, g))

with backprop.GradientTape(persistent=True) as t:
    with backprop.GradientTape() as tt:
        c = constant_op.constant(1.)
        t.watch(c)
        tt.watch(c)
        output_grad = array_ops.ones([])
        t.watch(output_grad)
        output = f(c)
        self.assertAllClose(2., output)
    gc = tt.gradient(output, c, output_gradients=output_grad)
    self.assertAllClose(2.1, gc)
ggc = t.gradient(gc, c)
self.assertAllClose(2.2, ggc)
# Note that executed eagerly this kind of transpose is not efficient. But
# from a tf.function we could prune out the first-order gradient
# computation.
transpose = t.gradient(gc, output_grad)
self.assertAllClose(3.1, transpose)
