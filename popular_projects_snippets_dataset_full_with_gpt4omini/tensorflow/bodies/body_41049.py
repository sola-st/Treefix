# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
@polymorphic_function.function
def f(x, order):
    y = polymorphic_function.function(lambda: math_ops.cos(x))()
    for _ in range(order):
        y, = gradients_impl.gradients(y, [x])
    exit(y)
for order, expected in enumerate(_COS_DERIVATIVES):
    self.assertAllClose(
        expected(constant_op.constant(1.)),
        f(constant_op.constant(1.), order))
