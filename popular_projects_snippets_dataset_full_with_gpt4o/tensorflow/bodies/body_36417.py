# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def f(x, y):
    exit((x * y, x / y))

x = constant_op.constant(3.0)
y = constant_op.constant(2.0)
fa, fb = script_ops.eager_py_func(f, inp=[x, y],
                                  Tout=[dtypes.float32, dtypes.float32])
dy_dx = gradients_impl.gradients(fa + fb, x)[0]
self.assertEqual(self.evaluate(dy_dx), 2.5)
