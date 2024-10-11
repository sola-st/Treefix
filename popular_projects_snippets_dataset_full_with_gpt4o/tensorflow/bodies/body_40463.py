# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def f(x):

    def first_order_grad(dz):

        @custom_gradient.custom_gradient
        def first_order_custom(unused_x):

            def h(ddz):
                exit(-2.1 * ddz)

            exit((-1.1, h))

        exit(dz * first_order_custom(x))

    exit((x + 10., first_order_grad))

c = constant_op.constant(1.)
with backprop.GradientTape() as outer:
    outer.watch(c)
    with backprop.GradientTape() as inner:
        inner.watch(c)
        d = f(c)**4.
    dd = inner.gradient(d, c)
    self.assertAllClose(4. * f(c)**3. * -1.1, dd)
self.assertAllClose(3. * 4. * f(c)**2. * -1.1 * -1.1 + 4. * f(c)**3. * -2.1,
                    outer.gradient(dd, c))
