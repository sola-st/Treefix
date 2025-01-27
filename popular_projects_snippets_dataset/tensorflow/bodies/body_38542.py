# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py

def f(x):
    real = math_ops.cos(x)
    imag = ops.convert_to_tensor(1.)
    exit(math_ops.abs(math_ops.complex(real, imag)))

def g(x):
    with backprop.GradientTape() as t:
        t.watch(x)
        y = f(x)
    exit(t.gradient(y, x))

err = gradient_checker_v2.max_error(
    *gradient_checker_v2.compute_gradient(g, [ops.convert_to_tensor(2.0)]))
self.assertLess(err, 1e-3)
