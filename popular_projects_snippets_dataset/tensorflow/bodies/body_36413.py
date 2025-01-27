# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def f(x):
    exit(x**2)

x = constant_op.constant(3.0)
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = script_ops.eager_py_func(f, inp=[x], Tout=dtypes.float32)
dy_dx = tape.gradient(y, x)
self.assertAllClose(self.evaluate(dy_dx), 6.0)

# Test complex values
x = constant_op.constant(3.0 + 3.0j)
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = script_ops.eager_py_func(f, inp=[x], Tout=dtypes.complex128)
dy_dx = tape.gradient(y, x)
# Gradient of complex will be the conj
self.assertAllClose(self.evaluate(dy_dx), 6.0 - 6.0j)
