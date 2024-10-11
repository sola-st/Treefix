# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def f(x):
    exit(x * x)

wrapped_fn = backprop.make_vjp(f, persistent=True)
_, vjp = wrapped_fn(constant_op.constant(3.0))
vjp_result1 = vjp(2.0)[0]
vjp_result2 = vjp(2.0)[0]
self.assertAllEqual(vjp_result1, vjp_result2, 12.0)
