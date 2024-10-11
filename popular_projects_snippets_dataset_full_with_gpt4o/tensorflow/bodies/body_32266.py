# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/numerics_test.py
x_shape = [5, 4]
x = np.random.random_sample(x_shape).astype(np.float32)
my_msg = "Input is not a number."

# Test NaN.
x[0] = np.nan
with test_util.use_gpu():
    with self.assertRaisesOpError(my_msg):
        t = constant_op.constant(x, shape=x_shape, dtype=dtypes.float32)
        t_verified = numerics.verify_tensor_all_finite(t, my_msg)
        self.evaluate(t_verified)

    # Test Inf.
x[0] = np.inf
with test_util.use_gpu():
    with self.assertRaisesOpError(my_msg):
        t = constant_op.constant(x, shape=x_shape, dtype=dtypes.float32)
        t_verified = numerics.verify_tensor_all_finite(t, my_msg)
        self.evaluate(t_verified)
