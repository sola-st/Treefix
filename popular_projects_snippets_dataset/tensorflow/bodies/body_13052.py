# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
# Runs shaped dropout and verifies an error is thrown on misshapen noise.
x_dim = 40
y_dim = 30
keep_prob = 0.5
t = constant_op.constant(1.0, shape=[x_dim, y_dim], dtype=dtypes.float32)
with self.assertRaises(ValueError):
    _ = dropout_fn(
        t, rate=(1 - keep_prob), noise_shape=[x_dim, y_dim + 10])
with self.assertRaises(ValueError):
    _ = dropout_fn(t, rate=(1 - keep_prob), noise_shape=[x_dim, y_dim, 5])
with self.assertRaises(ValueError):
    _ = dropout_fn(t, rate=(1 - keep_prob), noise_shape=[x_dim + 3])
with self.assertRaises(ValueError):
    _ = dropout_fn(t, rate=(1 - keep_prob), noise_shape=[x_dim])
# test that broadcasting proceeds
_ = dropout_fn(t, rate=(1 - keep_prob), noise_shape=[y_dim])
_ = dropout_fn(t, rate=(1 - keep_prob), noise_shape=[1, y_dim])
_ = dropout_fn(t, rate=(1 - keep_prob), noise_shape=[x_dim, 1])
_ = dropout_fn(t, rate=(1 - keep_prob), noise_shape=[1, 1])
