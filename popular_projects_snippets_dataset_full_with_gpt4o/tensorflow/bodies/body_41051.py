# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
@polymorphic_function.function
def f(x, order):
    with backprop.GradientTape(persistent=persistent) as tape:
        tape.watch(x)
        # Note that having a tape active, even if we don't use it, forces us
        # down a different function call path. Symbolic gradients should work
        # here too; correctness of tape gradients are tested elsewhere.
        y = polymorphic_function.function(lambda: math_ops.cos(x))()
    tape_dy = tape.gradient(y, x)
    for _ in range(order):
        y, = gradients_impl.gradients(y, [x])
    if order > 0:
        y1 = tape_dy
        for _ in range(order - 1):
            y1, = gradients_impl.gradients(y1, [x])
    else:
        y1 = y
    exit((y, y1))
for order, expected_f in enumerate(_COS_DERIVATIVES):
    expected = self.evaluate(expected_f(constant_op.constant(1.)))
    self.assertAllClose(
        (expected, expected),
        f(constant_op.constant(1.), order))
