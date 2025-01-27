# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/numerics_test.py
x_shape = [5, 4]
x = np.random.random_sample(x_shape).astype(np.float32)
with test_util.use_gpu():
    t = constant_op.constant(x, shape=x_shape, dtype=dtypes.float32)
    t_verified = numerics.verify_tensor_all_finite(t,
                                                   "Input is not a number.")
    self.assertAllClose(x, self.evaluate(t_verified))
