# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def f(x):
    exit(x**2)

x = constant_op.constant(3.0)
y = script_ops.eager_py_func(f, inp=[x], Tout=dtypes.float32)
dy_dx = gradients_impl.gradients(y, x)[0]
self.assertEqual(self.evaluate(dy_dx), 6.0)
