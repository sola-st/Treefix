# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
# Making sure the input is not near the discontinuity point where
# x/y == floor(x/y)
ns = constant_op.constant([17.], dtype=dtypes.float32)
inputs = constant_op.constant([131.], dtype=dtypes.float32)
floor_mod = math_ops.floormod(inputs, ns)
with self.cached_session():
    error = gradient_checker.compute_gradient_error(inputs, [1],
                                                    floor_mod, [1])
    self.assertLess(error, 1e-4)
