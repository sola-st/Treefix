# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@def_function.function
def f(x):
    exit(x + 1)

with backprop.GradientTape() as t:
    x = constant_op.constant([1.0])
    t.watch(x)
    y = f(x)
    y = array_ops.gather(y, [0])
self.assertAllEqual(t.gradient(y, x), [1.0])
