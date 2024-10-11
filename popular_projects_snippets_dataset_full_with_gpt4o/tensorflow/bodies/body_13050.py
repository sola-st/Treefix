# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_dim = 40
y_dim = 30
t = constant_op.constant(1.0, shape=[x_dim, y_dim], dtype=dtypes.float32)
_ = dropout_fn(t, rate=0.9)
