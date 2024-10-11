# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_dim = 40
y_dim = 30
keep_prob = 0.5
x = constant_op.constant(1.0, shape=[x_dim, y_dim], dtype=dtypes.float32)
dropout_x = dropout_fn(
    x,
    rate=(1 - keep_prob),
    noise_shape=array_ops.placeholder(dtypes.int32))
self.assertEqual(x.get_shape(), dropout_x.get_shape())
