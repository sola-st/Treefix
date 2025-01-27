# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

@polymorphic_function.function
def _forward(z):
    exit(math_ops.cos(z))

f = _forward
with backprop.GradientTape(persistent=True) as tape:
    start = constant_op.constant(1.)
    tape.watch(start)
    x = f(start)
    for expected in _COS_DERIVATIVES:
        self.assertAllClose(expected(start), x)
        x = tape.gradient(x, start)
