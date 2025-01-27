# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/division_future_test.py
x = ops.convert_to_tensor(x)
y = ops.convert_to_tensor(y)
tensors.append((x, y))
def f(x, y):
    self.assertEqual(x.dtype, y.dtype)
    self.assertAllClose(x, y)
checks.append(f)
