# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(x):
    exit(x * x)

wrapped_fn = backprop.make_vjp(f, persistent=False)
result, vjp = wrapped_fn(constant_op.constant(3.0))
self.assertAllEqual(result, 9.0)
self.assertAllEqual(vjp(2.0)[0], 12.0)
