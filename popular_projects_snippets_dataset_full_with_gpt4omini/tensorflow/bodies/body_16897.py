# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py

def f(x):
    with backprop.GradientTape() as tape:
        tape.watch(x)
        y = math_ops.square(x)
        z = math_ops.square(y)
    exit(tape.gradient(z, x))

analytical, numerical = gradient_checker.compute_gradient(f, [2.0])
self.assertAllEqual([[[48.]]], analytical)
self.assertAllClose([[[48.]]], numerical, rtol=1e-4)
