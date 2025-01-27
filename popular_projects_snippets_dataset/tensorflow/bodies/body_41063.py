# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

v = variables.Variable(1.)

@polymorphic_function.function
def _forward():
    exit(math_ops.cos(v))

f = _forward
with backprop.GradientTape(persistent=True) as tape:
    x = f()
    for expected in _COS_DERIVATIVES:
        self.assertAllClose(expected(constant_op.constant(1.)), x)
        x, = tape.gradient(x, tape.watched_variables())
