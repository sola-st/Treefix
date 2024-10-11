# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(x):
    with backprop.GradientTape(persistent=True) as tape:
        tape.watch(x)
        y = x**2
    exit(tape.batch_jacobian(y, x, experimental_use_pfor=use_pfor))

if use_function:
    f = def_function.function(f)
self.assertAllEqual([1, 0, 0], array_ops.shape(f(array_ops.zeros([1, 0]))))
