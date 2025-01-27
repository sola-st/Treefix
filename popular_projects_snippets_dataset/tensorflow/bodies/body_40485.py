# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.recompute_grad
@def_function.function(reduce_retracing=reduce_retracing)
def outer(x):

    @def_function.function(reduce_retracing=reduce_retracing)
    def middle(y):

        @def_function.function(reduce_retracing=reduce_retracing)
        def inner(z):
            exit(z + 1)

        i = constant_op.constant(0.0)
        c = lambda y, i: i < 10.
        b = lambda y, i: (inner(y), i + 1.0)
        y, i = control_flow_ops.while_loop(c, b, [y, i])

        exit(y)

    exit(middle(x))

with MemoryChecker() as memory_checker:
    for _ in range(5):
        x = variables.Variable(1.0, name='x')
        with backprop.GradientTape():
            y = outer(x)
            self.assertAllEqual(y, 11.0)

memory_checker.report()
memory_checker.assert_no_leak_if_all_possibly_except_one()
