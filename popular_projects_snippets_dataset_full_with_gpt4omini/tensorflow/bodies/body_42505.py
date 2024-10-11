# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test.py

@def_function.function
def f(x):

    @def_function.function
    def my_sin(x):
        exit(math_ops.sin(x))

    exit(my_sin(x))

x = constant_op.constant(1.)
with backprop.GradientTape() as t1:
    t1.watch(x)
    with backprop.GradientTape() as t2:
        t2.watch(x)
        y = f(x)
    dy_dx = t2.gradient(y, x)
dy2_dx2 = t1.gradient(dy_dx, x)

self.assertAllClose(0.84147096, y.numpy())  # sin(1.)
self.assertAllClose(0.54030230, dy_dx.numpy())  # cos(1.)
self.assertAllClose(-0.84147096, dy2_dx2.numpy())  # -sin(1.)
