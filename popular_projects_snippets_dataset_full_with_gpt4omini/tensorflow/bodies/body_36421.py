# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def f(x, y):
    exit(x**2 + y**2)

x = constant_op.constant(3.0)
y = constant_op.constant(4.0)
z = script_ops.eager_py_func(f, inp=[x, y], Tout=dtypes.float32)

dz_dx, dz_dy = gradients_impl.gradients(z, [x, y])
self.assertEqual(self.evaluate(dz_dx), 6.0)
self.assertEqual(self.evaluate(dz_dy), 8.0)
